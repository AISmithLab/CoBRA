<p align="center">
  <img src="figures/Cobra.png" alt="CoBRA Logo" width="400"/>
</p>

# Toward Precise and Consistent Agent Behaviors across Models

<p align="center">
  <a href="https://arxiv.org/abs/2509.13588"><img src="https://img.shields.io/badge/arXiv-2509.13588-b31b1b.svg" alt="arXiv"></a>
  <a href="https://doi.org/10.48550/arXiv.2509.13588"><img src="https://img.shields.io/badge/DOI-10.48550/arXiv.2509.13588-blue" alt="DOI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-green.svg" alt="License"></a>
</p>



> 📄 **Paper**: [arXiv:2509.13588](https://arxiv.org/abs/2509.13588) - *CoBRA: Programming Cognitive Bias in Social Agents Using Classic Social Science Experiments*

**📖 Language / 语言**: [简体中文](README_zh-CN.md)

---

> **💡 What is Cognitive Bias?**
> 
> Cognitive bias refers to systematic deviations from rational judgment in human cognition and 
decision-making. For example, *Framing Effect*: "90% survival rate" vs. "10% mortality rate" — logically identical, yet people make different choices based on how information is framed.

---

**CoBRA**(**Co**gnitive **B**ias **R**egulator for Social **A**gents) harnesses the structured and validated social science experiments as the calibration toolkit to control and align model behaviors across models.

At the heart of CoBRA is a novel closed-loop system primitive with two components: (1) Cognitive Bias Index that measures the demonstrated cognitive bias of a social agent, by quantifying the agent's reactions in a set of validated classic social science experiments; (2) Behavioral Regulation Engine that aligns the agent's behavior to exhibit controlled cognitive bias. Through CoBRA, we show how to operationalize validated social science knowledge (i.e., classical experiments) as reusable "gym" environments for AI -- an approach that may generalize to richer social and affective simulations beyond bias alone.


## The Problem and Our Solution

<p align="center">
  <img src="figures/fig1.png" alt="CoBRA Overview" width="800"/>
  <br>
</p>

Existing social simulation experiments use implicit natural-language descriptions to specify agent behaviors, leading to inconsistent and unpredictable outcomes across models. For instance, a social simulation might expect agents playing economist roles to be less susceptible to framing effects than agents playing the general population roles; however, agents with implicit specifications fail to reliably demonstrate such behavioral differences.

**CoBRA solves this by enabling researchers to explicitly and quantitatively control the amount of cognitive biases exhibited in social agents' observable behaviors.**

---

**CoBRA provides three control methods:**
- **Prompt Engineering** (input space control)
- **Representation Engineering** (activation space control)  
- **Fine-tuning** (parameter space control)

<p align="center">
  <img src="figures/fig2.png" alt="CoBRA Workflow" width="800"/>
  <br>
  <em>Example: A researcher specifies a target bias level → CoBRA measures it via classic experiments → iteratively adjusts the agent until it reliably exhibits the desired bias.</em>
</p>

### More Visual Overview


<details>
<summary><b>Click to see more technical diagrams</b></summary>

<p align="center">
  <img src="figures/fig5.png" alt="Classic Social Experiment Testbed" width="800"/>
  <br>
  <em>Figure 5: Cognitive Bias Index measures agent behavior through validated classic social experiments.</em>
</p>

<p align="center">
  <img src="figures/fig6.png" alt="Behavioral Regulation Engine" width="800"/>
  <br>
  <em>Figure 6: Behavioral Regulation Engine provides three control methods across input, activation, and parameter spaces.</em>
</p>

</details>

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
├── generator/                  # Data generation utilitiesn
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

**Paper Links:**
- arXiv: [https://arxiv.org/abs/2509.13588](https://arxiv.org/abs/2509.13588)
- DOI: [https://doi.org/10.48550/arXiv.2509.13588](https://doi.org/10.48550/arXiv.2509.13588)

## License

MIT License - see [`LICENSE`](LICENSE) for details

## Contact

- **Lead Author**: Xuan Liu (xul049@ucsd.edu)
- **GitHub Issues**: [Report bugs or request features](https://github.com/AISmithLab/CoBRA/issues)

---

**Need help?** Check [`examples/unified_bias/README.md`](examples/unified_bias/README.md) for detailed walkthroughs. The finetuning code is in the `finetuning` branch.
