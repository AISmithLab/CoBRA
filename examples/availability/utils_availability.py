# utils_availability.py

import json
import random
import numpy as np


def load_availability_scenarios(data_path, scenario_type, num_scenarios=None):
    """
    Loads availability heuristic scenarios from seed data JSON files.

    Args:
        data_path: Path to JSON file
            (e.g., availability_judgment_of_word_frequency.json or
             availability_fame_frequency_and_recall.json)
        scenario_type: 'judgment_of_word_frequency' or 'fame_frequency_and_recall'
        num_scenarios: Optional limit on number of scenarios returned

    Returns:
        List of scenario dicts whose keys match prompt template placeholders:
        - judgment_of_word_frequency: {id, unit, source}
        - fame_frequency_and_recall: {id, domain, group_a, group_b, list_of_names}
    """
    with open(data_path, 'r') as f:
        data = json.load(f)

    if num_scenarios is not None and len(data) > num_scenarios:
        data = data[:num_scenarios]

    scenarios = []

    if scenario_type == 'judgment_of_word_frequency':
        for item in data:
            scenarios.append({
                "id": item["id"],
                "unit": item["unit"],
                "source": item["source"]
            })

    elif scenario_type == 'fame_frequency_and_recall':
        for item in data:
            # Convert names_list array to a single string for prompt insertion
            names_list = item.get("names_list", [])
            names_string = "\n".join(names_list) if isinstance(names_list, list) else str(names_list)

            scenarios.append({
                "id": item["id"],
                "domain": item["domain"],
                "group_a": item["group_a_label"],
                "group_b": item["group_b_label"],
                "list_of_names": names_string
            })
    else:
        print(f"Unknown scenario type: {scenario_type}")
        return []

    return scenarios


def create_availability_dataset(data_path: str, tokenizer, user_tag: str = "USER: ",
                                assistant_tag: str = "ASSISTANT: ", seed: int = 42,
                                testing: bool = False) -> dict:
    """
    Creates RepE training dataset from original hand-crafted availability data.

    Generates positive (availability-biased) and negative (statistical-reasoning)
    persona-based prompts for training a RepReader.
    """
    random.seed(seed)
    with open(data_path, 'r') as f:
        data = json.load(f)

    # Define persona templates
    positive_persona_template = (
        "Pretend you are very prone to availability bias, always judging frequency "
        "and probability based on how easily examples come to mind. \n\n{availability_scenario}"
    )
    neutral_persona_template = "{availability_scenario}"
    negative_persona_template = (
        "Pretend you are not prone to availability bias, never judging frequency "
        "based on ease of recall; always rely on actual statistics. \n\n{availability_scenario}"
    )

    persona_pair_definitions = [
        (positive_persona_template, neutral_persona_template),
        (neutral_persona_template, negative_persona_template),
    ]

    all_generated_pairs = []

    for item in data:
        # Build a simple prompt from the seed data fields
        if "unit" in item:
            base_prompt = (
                f"Consider the letter/prefix \"{item['unit']}\". "
                f"If you sampled a random {item['source']}, is it more likely to "
                f"appear in the first position or the third position?"
            )
        elif "domain" in item:
            names_list = item.get("names_list", [])
            names_string = "\n".join(names_list) if isinstance(names_list, list) else str(names_list)
            base_prompt = (
                f"You are presented with the following list of {item['domain']} names:\n"
                f"{names_string}\n\n"
                f"Some belong to {item['group_a_label']}. "
                f"The others belong to {item['group_b_label']}. "
                f"Which group appeared more often in the list?"
            )
        else:
            continue

        for preferred_template, rejected_template in persona_pair_definitions:
            preferred_user_prompt = preferred_template.format(availability_scenario=base_prompt)
            rejected_user_prompt = rejected_template.format(availability_scenario=base_prompt)

            # For hand-crafted data we use a simple answer token expansion
            answer_text = "A"
            tokens = tokenizer.tokenize(answer_text)
            if not tokens:
                positive_examples = [f"{user_tag}{preferred_user_prompt}{assistant_tag}"]
                negative_examples = [f"{user_tag}{rejected_user_prompt}{assistant_tag}"]
            else:
                positive_examples = []
                negative_examples = []
                for idx in range(len(tokens) + 1):
                    assistant_part = "" if idx == 0 else tokenizer.convert_tokens_to_string(tokens[:idx])
                    positive_examples.append(f"{user_tag}{preferred_user_prompt}{assistant_tag}{assistant_part}")
                    negative_examples.append(f"{user_tag}{rejected_user_prompt}{assistant_tag}{assistant_part}")

            all_generated_pairs.extend(
                [[pos, neg] for pos, neg in zip(positive_examples, negative_examples)]
            )

    if not all_generated_pairs:
        print("No examples were generated. Check data paths and processing logic.")
        return {'train': {'data': [], 'labels': []}, 'test': {'data': [], 'labels': []}}

    # Combine and split data
    combined_data_true_pairs = all_generated_pairs
    random.shuffle(combined_data_true_pairs)

    num_pairs = len(combined_data_true_pairs)
    ntrain_pairs = int(num_pairs * 0.6) if not testing else num_pairs
    if ntrain_pairs == 0 and num_pairs > 0:
        ntrain_pairs = 1

    train_pairs = combined_data_true_pairs[:ntrain_pairs]
    test_pairs = combined_data_true_pairs[ntrain_pairs:]

    # Process TRAIN pairs
    train_data_flat = []
    train_labels = []
    for pos_example, neg_example in train_pairs:
        true_positive_example = pos_example
        shuffled_pair = [pos_example, neg_example]
        random.shuffle(shuffled_pair)
        train_data_flat.extend(shuffled_pair)
        train_labels.append([s == true_positive_example for s in shuffled_pair])

    # Process TEST pairs
    test_data_flat = []
    test_labels = []
    for pos_example, neg_example in test_pairs:
        true_positive_example = pos_example
        shuffled_pair = [pos_example, neg_example]
        random.shuffle(shuffled_pair)
        test_data_flat.extend(shuffled_pair)
        test_labels.append([s == true_positive_example for s in shuffled_pair])

    return {
        'train': {'data': train_data_flat, 'labels': train_labels},
        'test': {'data': test_data_flat, 'labels': test_labels}
    }


def create_availability_dataset_from_generated(data_path: str, tokenizer,
                                               user_tag: str = "USER: ",
                                               assistant_tag: str = "ASSISTANT: ",
                                               seed: int = 42, testing: bool = False,
                                               model_name: str = None) -> dict:
    """
    Processes generated availability bias data from the generator format.
    Handles data generated by scenario_generator.py and response_generator.py.
    """
    random.seed(seed)
    with open(data_path, 'r') as f:
        data = json.load(f)

    # Define persona templates for generating contrasting pairs
    positive_persona_template = (
        "Pretend you are very prone to availability bias, always judging frequency "
        "and probability based on how easily examples come to mind. \n\n{scenario_prompt}"
    )
    neutral_persona_template = "{scenario_prompt}"
    negative_persona_template = (
        "Pretend you are not prone to availability bias, never judging frequency "
        "based on ease of recall; always rely on actual statistics. \n\n{scenario_prompt}"
    )

    persona_pair_definitions = [
        (positive_persona_template, neutral_persona_template),
        (neutral_persona_template, negative_persona_template),
    ]

    all_generated_pairs = []

    for item in data:
        scenario_text = item.get("scenario", "")
        bias_type = item.get("bias_type", "availability")

        if bias_type != "availability":
            continue

        full_scenario_prompt = scenario_text

        for preferred_template, rejected_template in persona_pair_definitions:
            preferred_user_prompt = preferred_template.format(scenario_prompt=full_scenario_prompt)
            rejected_user_prompt = rejected_template.format(scenario_prompt=full_scenario_prompt)

            # Collect responses
            responses_to_use = []

            if 'responses' in item:
                for response_key, response_data in item['responses'].items():
                    if isinstance(response_data, dict) and 'text' in response_data:
                        response_text = response_data['text']
                        if response_text and response_text.strip():
                            responses_to_use.append(response_text.strip())

                if model_name:
                    model_responses = []
                    for response_key, response_data in item['responses'].items():
                        if (isinstance(response_data, dict) and
                            'model_used' in response_data and
                            response_data['model_used'] == model_name and
                            'text' in response_data):
                            model_responses.append(response_data['text'].strip())
                    if model_responses:
                        responses_to_use = model_responses

            if not responses_to_use:
                error_msg = (
                    f"No generated response found for item {item.get('id', 'unknown')}. "
                    f"Generated data must contain valid responses."
                )
                if testing:
                    print(f"[ERROR] {error_msg}")
                raise ValueError(error_msg)

            for response_text in responses_to_use:
                tokens = tokenizer.tokenize(response_text)
                if not tokens:
                    positive_examples = [f"{user_tag}{preferred_user_prompt}{assistant_tag}"]
                    negative_examples = [f"{user_tag}{rejected_user_prompt}{assistant_tag}"]
                else:
                    positive_examples = []
                    negative_examples = []
                    for idx in range(len(tokens) + 1):
                        assistant_part = "" if idx == 0 else tokenizer.convert_tokens_to_string(tokens[:idx])
                        positive_examples.append(f"{user_tag}{preferred_user_prompt}{assistant_tag}{assistant_part}")
                        negative_examples.append(f"{user_tag}{rejected_user_prompt}{assistant_tag}{assistant_part}")

                all_generated_pairs.extend(
                    [[pos, neg] for pos, neg in zip(positive_examples, negative_examples)]
                )

    if not all_generated_pairs:
        print("No examples were generated from the data. Check data format and processing logic.")
        return {'train': {'data': [], 'labels': []}, 'test': {'data': [], 'labels': []}}

    # Split into train/test sets
    combined_data_true_pairs = all_generated_pairs
    random.shuffle(combined_data_true_pairs)

    num_available_pairs = len(combined_data_true_pairs)
    ntrain_pairs = int(num_available_pairs * 0.6) if not testing else 128
    if ntrain_pairs == 0 and num_available_pairs > 0:
        ntrain_pairs = 1
    if num_available_pairs == 0:
        print("No pairs could be formed for training.")
        return {'train': {'data': [], 'labels': []}, 'test': {'data': [], 'labels': []}}

    train_data_selected_pairs = combined_data_true_pairs[:ntrain_pairs]
    train_labels = []
    train_data_flat_list = []

    for d_pair in train_data_selected_pairs:
        true_positive_example = d_pair[0]
        shuffled_current_pair = list(d_pair)
        random.shuffle(shuffled_current_pair)
        train_data_flat_list.extend(shuffled_current_pair)
        train_labels.append([s == true_positive_example for s in shuffled_current_pair])

    train_data = train_data_flat_list

    # Create test data from remaining pairs
    remaining_true_pairs = combined_data_true_pairs[ntrain_pairs:]
    test_data = []
    test_labels = []

    if len(remaining_true_pairs) > 1:
        mismatched_test_pairs_list = []
        for i in range(len(remaining_true_pairs) - 1):
            pos_from_pair_i = remaining_true_pairs[i][0]
            neg_from_pair_i_plus_1 = remaining_true_pairs[i + 1][1]
            mismatched_test_pairs_list.append([pos_from_pair_i, neg_from_pair_i_plus_1])

        num_mismatched_test_pairs_to_take = min(256, len(mismatched_test_pairs_list))
        selected_mismatched_pairs_for_test = mismatched_test_pairs_list[:num_mismatched_test_pairs_to_take]
        if selected_mismatched_pairs_for_test:
            test_data = np.concatenate(selected_mismatched_pairs_for_test).tolist()
        test_labels = [[True, False]] * len(selected_mismatched_pairs_for_test)

    return {
        'train': {'data': train_data, 'labels': train_labels},
        'test': {'data': test_data, 'labels': test_labels}
    }
