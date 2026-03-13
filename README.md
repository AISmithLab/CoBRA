<p align="center">
  <img src="figures/Cobra.png" alt="CoBRA Logo" width="400"/>
</p>

<p align="center">
  <a href="https://chi2026.acm.org/"><img src="https://img.shields.io/badge/🏆_CHI_2026-Best_Paper_Award-gold.svg" alt="CHI 2026 Best Paper Award"></a>
  <a href="https://arxiv.org/abs/2509.13588"><img src="https://img.shields.io/badge/arXiv-2509.13588-b31b1b.svg" alt="arXiv"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <img src="https://img.shields.io/badge/🚧_Status-Under_Active_Development-orange.svg" alt="Under Active Development">
</p>

<h3 align="center"><em>Toward Precise and Consistent Agent Behaviors across Models Anchored by Validated Social Science Knowledge</em></h3>

<p align="center">
  🌐 <b>Project Page</b>: <a href="https://cobra.clawder.ai">cobra.clawder.ai</a> &nbsp;|&nbsp;
  📄 <b>Paper</b>: <a href="https://arxiv.org/abs/2509.13588">arXiv 2509.13588</a>
</p>

<p align="center"><strong>If you find CoBRA useful, please star ⭐ this repo to help others discover it!</strong></p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/lang-English-blue.svg" alt="English"></a>
  <a href="README_zh-CN.md"><img src="https://img.shields.io/badge/lang-简体中文-red.svg" alt="简体中文"></a>
</p>

<video src="https://github.com/user-attachments/assets/028ca8f4-6edd-426e-b436-2c3b796d81a0" controls width="700"></video>

> **💡 What is Cognitive Bias?**
> 
> Systematic deviations from rational judgment in human cognition and decision-making. For example, *Framing Effect*: "90% survival rate" vs. "10% mortality rate" — logically identical, yet people make different choices based on how information is framed.

---

Reproducibility and controllability are fundamental to scientific research. Yet implicit natural language descriptions — the dominant approach for specifying social agent behaviors in nearly all LLM-based social simulations — often fail to yield consistent behavior across models or capture the nuances of the descriptions.

**CoBRA** (**Co**gnitive **B**ias **R**egulator for Social **A**gents) is a novel toolkit that lets researchers explicitly specify desired nuances in LLM-based agents and obtain consistent behavior across models.

Through CoBRA, we show how to **operationalize validated social science knowledge as reusable "gym" environments for AI** — an approach that generalizes to richer social and affective simulations.

<p align="center">
  <img src="figures/fig1.png" alt="CoBRA Overview" width="800"/>
  <br>
  <em>The problem and our solution: from inconsistent agent behaviors under implicit specifications to explicit, quantitative control.</em>
</p>

---

**At the heart of CoBRA is a novel closed-loop system with two core components:**
- **Cognitive Bias Index** — measures the cognitive bias of a social agent by quantifying its reactions in validated classic social science experiments
- **Behavioral Regulation Engine** — aligns the agent's behavior to exhibit controlled cognitive bias, via three control methods:
  - **Prompt Engineering** (input space control)
  - **Representation Engineering** (activation space control)
  - **Fine-tuning** (parameter space control)

<p align="center">
  <img src="figures/fig2.png" alt="CoBRA Workflow" width="800"/>
  <br>
  <em>Example: A researcher specifies a target bias level → CoBRA measures it via classic experiments → iteratively adjusts the agent until it reliably exhibits the desired bias.</em>
</p>


## Quick Start (3 Steps)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Navigate to the unified bias control module
cd examples/unified_bias

# 3. Run a bias experiment
python pipelines.py --bias authority --method repe-linear --model Mistral-7B
```

**That's it.** The system will measure and control the agent's Authority Effect bias.

## Repository Structure

```
CoBRA/
├── control/                    # Core bias control engine
├── examples/
│   ├── unified_bias/           # Main entry point (START HERE)
│   │   ├── pipelines.py        # Unified experiment runner
│   │   ├── run_pipelines.py    # CLI interface
│   │   ├── ablation/           # Ablation studies
│   │   └── README.md           # Full usage guide
│   ├── authority/              # Authority Effect utils
│   ├── bandwagon/              # Bandwagon Effect utils
│   ├── confirmation/           # Confirmation Bias utils
│   └── framing/                # Framing Effect utils
├── generator/                  # Data generation utilities
├── data_generated/             # Generated experimental data
├── webdemo/                    # Web demonstration interface
└── requirements.txt            # Python dependencies
```

## Key Components

| Component | Description | Documentation |
|-----------|-------------|---------------|
| **Cognitive Bias Index** | Measures bias strength via classic experiments | [`data/data_README.md`](data/data_README.md) |
| **Behavioral Regulation Engine** | Three control methods (Prompt/RepE/Finetune) | [`control/control_README.md`](control/control_README.md) |
| **Unified Pipeline** | Run full experiments with one command | [`examples/unified_bias/README.md`](examples/unified_bias/README.md) |
| **Ablation Studies** | Test model/persona/temperature sensitivity | [`examples/unified_bias/ablation/README.md`](examples/unified_bias/ablation/README.md) |
| **Data Generator** | Create custom bias scenarios and responses | [`generator/README.md`](generator/README.md) |

## Supported Biases & Experiments

| Bias Type | Paradigms | Data Directory | Control Range |
|-----------|-----------|----------------|---------------|
| **Authority Effect** | Milgram Obedience, Stanford Prison | [`data/authority/`](data/authority/) | 0-4 scale |
| **Bandwagon Effect** | Asch's Line, Hotel Towel | [`data/bandwagon/`](data/bandwagon/) | 0-4 scale |
| **Confirmation Bias** | Wason Selection, Biased Information | [`data/confirmation/`](data/confirmation/) | 0-4 scale |
| **Framing Effect** | Asian Disease, Investment/Insurance | [`data/framing/`](data/framing/) | 0-4 scale |


## Citation

If you use CoBRA in your research, please cite our paper:

```bibtex
@misc{liu2026cobraprogrammingcognitivebias,
      title={CoBRA: Programming Cognitive Bias in Social Agents Using Classic Social Science Experiments}, 
      author={Xuan Liu and Haoyang Shang and Haojian Jin},
      year={2026},
      eprint={2509.13588},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2509.13588}, 
}
```

**Paper Link:** [https://arxiv.org/abs/2509.13588](https://arxiv.org/abs/2509.13588)

## License

MIT License - see [`LICENSE`](LICENSE) for details

## Contact

For questions, please contact the corresponding author Xuan Liu at xul049@ucsd.edu, or file a [GitHub Issue](https://github.com/AISmithLab/CoBRA/issues) to report bugs and request features.

---

**Need help?** Check [`examples/unified_bias/README.md`](examples/unified_bias/README.md) for detailed walkthroughs. The finetuning code is in the `finetuning` branch.

