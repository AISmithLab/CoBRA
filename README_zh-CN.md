<p align="center">
  <img src="figures/Cobra.png" alt="CoBRA Logo" width="400"/>
</p>

## 以经验证的社会科学知识为准绳实现跨模型精确一致的智能体行为

<p align="center">
  <a href="https://arxiv.org/abs/2509.13588"><img src="https://img.shields.io/badge/arXiv-2509.13588-b31b1b.svg" alt="arXiv"></a>
  <a href="https://doi.org/10.48550/arXiv.2509.13588"><img src="https://img.shields.io/badge/DOI-10.48550/arXiv.2509.13588-blue" alt="DOI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-green.svg" alt="License"></a>
</p>

> 📄 **论文**: [arXiv:2509.13588](https://arxiv.org/abs/2509.13588) - *CoBRA: Programming Cognitive Bias in Social Agents Using Classic Social Science Experiments*


**📖 Language / 语言**: [English](README.md) 

---

> **💡 什么是认知偏差？**
> 
> 认知偏差是指人类在认知和决策过程中系统性地偏离理性判断的现象。例如*框架效应*："90% 存活率" vs. "10% 死亡率" —— 逻辑等价，但人们会因表述方式不同而做出不同决策。

---

**CoBRA**（**Co**gnitive **B**ias **R**egulator for Social **A**gents / 社交智能体认知偏差调节器）通过结构化且经过验证的社会科学实验，实现跨模型的智能体行为控制与对齐。

CoBRA 的核心是一套创新的闭环控制系统，包含两个关键模块：(1) **认知偏差指数** —— 基于经典社会科学实验测量智能体的认知偏差水平；(2) **行为调节引擎** —— 精确调控智能体表现出的认知偏差程度。通过 CoBRA，我们展示了如何将经过验证的社会科学知识（即经典实验）转化为可复用的 AI 训练环境——这一方法不仅适用于认知偏差，还可推广到更丰富的社交与情感模拟场景。


## 问题与解决方案

<p align="center">
  <img src="figures/fig1.png" alt="CoBRA Overview" width="800"/>
  <br>
</p>

现有的社交模拟实验使用隐式的自然语言描述来指定智能体行为，导致跨模型的结果不一致且不可预测。例如，社交模拟可能期望扮演经济学家角色的智能体比扮演普通大众角色的智能体更不容易受到框架效应的影响；然而，基于隐式规范的智能体无法可靠地展现这种行为差异。

**CoBRA 通过使研究人员能够明确且定量地控制社交智能体可观察行为中展现的认知偏差程度来解决这一问题。**

---

**CoBRA 提供三种控制方法:**
- **提示工程** (输入空间控制)
- **表示工程** (激活空间控制)  
- **微调** (参数空间控制)

<p align="center">
  <img src="figures/fig2.png" alt="CoBRA Workflow" width="800"/>
  <br>
  <em>示例：研究人员指定目标偏差水平 → CoBRA 通过经典实验测量 → 迭代调整智能体直到其可靠地展现所需偏差。</em>
</p>


## 快速开始（3步）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 进入统一偏差控制模块
cd examples/unified_bias

# 3. 运行偏差实验
python pipelines.py --bias authority --method repe-linear --model Mistral-7B
```

**就这样。** 系统将测量和控制智能体的权威效应偏差。

## 仓库结构

```
CoBRA/
├── control/                    # 核心偏差控制引擎
├── examples/
│   ├── unified_bias/           # 主要入口（从这里开始）
│   │   ├── pipelines.py        # 统一实验运行器
│   │   ├── run_pipelines.py    # 命令行界面
│   │   ├── ablation/           # 消融研究
│   │   └── README.md           # 完整使用指南
│   ├── authority/              # 权威效应工具
│   ├── bandwagon/              # 从众效应工具
│   ├── confirmation/           # 确认偏差工具
│   └── framing/                # 框架效应工具
├── generator/                  # 数据生成工具
├── data_generated/             # 生成的实验数据
├── webdemo/                    # Web 演示界面
└── requirements.txt            # Python 依赖
```

## 关键组件

| 组件 | 描述 | 文档 |
|------|------|------|
| **认知偏差指数** | 通过经典实验测量偏差强度 | [`data/data_README.md`](data/data_README.md) |
| **行为调节引擎** | 三种控制方法（提示/表示工程/微调） | [`control/control_README.md`](control/control_README.md) |
| **统一流程** | 用一条命令运行完整实验 | [`examples/unified_bias/README.md`](examples/unified_bias/README.md) |
| **消融研究** | 测试模型/角色/温度敏感性 | [`examples/unified_bias/ablation/README.md`](examples/unified_bias/ablation/README.md) |
| **数据生成器** | 创建自定义偏差场景和响应 | [`generator/README.md`](generator/README.md) |

## 支持的偏差类型与实验

| 偏差类型 | 实验范式 | 数据目录 | 控制范围 |
|---------|---------|---------|---------|
| **权威效应** | 米尔格拉姆服从实验、斯坦福监狱实验 | [`data/authority/`](data/authority/) | 0-4 量表 |
| **从众效应** | 阿希线段实验、酒店毛巾实验 | [`data/bandwagon/`](data/bandwagon/) | 0-4 量表 |
| **确认偏差** | 沃森选择任务、偏向信息实验 | [`data/confirmation/`](data/confirmation/) | 0-4 量表 |
| **框架效应** | 亚洲疾病问题、投资/保险问题 | [`data/framing/`](data/framing/) | 0-4 量表 |


## 引用

如果您在研究中使用 CoBRA，请引用我们的论文：

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

**论文链接：**
- arXiv: [https://arxiv.org/abs/2509.13588](https://arxiv.org/abs/2509.13588)
- DOI: [https://doi.org/10.48550/arXiv.2509.13588](https://doi.org/10.48550/arXiv.2509.13588)

## 许可证

MIT License - 详见 [`LICENSE`](LICENSE) 文件

## 联系方式

- **主要作者**: Xuan Liu (xul049@ucsd.edu)
- **GitHub Issues**: [报告 Bug 或请求新功能](https://github.com/AISmithLab/CoBRA/issues)

---

**需要帮助？** 查看 [`examples/unified_bias/README.md`](examples/unified_bias/README.md) 获取详细教程。微调代码位于 `finetuning` 分支。
