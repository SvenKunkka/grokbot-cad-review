<!-- SVENKUNKKA-README-NAV:BEGIN -->
[English overview](#project-overview-en) · [中文项目说明](#project-overview-zh) · [Maintainer on X / 维护者 X](https://x.com/Svenu1s5)
<!-- SVENKUNKKA-README-NAV:END -->

<!-- SVENKUNKKA-PROJECT-INFO:BEGIN -->

<a id="project-overview-en"></a>
## English project overview

A lightweight evidence-gathering tool for STEP reviews, reporting bounding boxes, volume, surface area, face counts, and a coarse draft check relative to the pull direction, with an AI review workflow.

**Getting started:** Install `cadquery`, then run `python scripts/step_summary.py part.step --pull z --min-draft 1.0`. See `SKILL.md` for the review workflow.

**Scope:** Coarse checks do not replace precise wall-thickness or undercut analysis, or physical validation; consult the upstream tools listed in the original README for deeper analysis.

**Repository maintainer / 仓库维护者:** [SvenKunkka](https://github.com/SvenKunkka) · [X / Twitter](https://x.com/Svenu1s5)

<a id="project-overview-zh"></a>
## 中文项目说明

面向 STEP 结构评审的轻量几何取证工具，输出实体包围盒、体积、表面积、面数及相对开模方向的拔模粗检，配套 AI 评审流程。

**使用入口：** 安装 `cadquery` 后运行 `python scripts/step_summary.py part.step --pull z --min-draft 1.0`，评审步骤见 `SKILL.md`。

**范围说明：** 粗检不能替代精确壁厚、倒扣分析或实物验证；复杂分析可参考原文列出的上游工具。

<!-- SVENKUNKKA-PROJECT-INFO:END -->

---



# grokbot-cad-review
STEP 结构评审的快速几何摘要工具，供 AI 做开模前评审时取证。

## 优先复用的上游
- [pzfreo/augura](https://github.com/pzfreo/augura)：基于 B-Rep 的壁厚 / 悬垂分析（3D 打印方向）
- [connorkapoor/Palmetto](https://github.com/connorkapoor/Palmetto)：注塑 DFM（壁厚、拔模角、倒扣）
- [CadQuery](https://github.com/cadquery/cadquery)（Apache-2.0）/ OCP：读取 STEP

本仓库只提供 `scripts/step_summary.py`：输出每个实体的包围盒、体积、表面积、面数和拔模角粗检（相对开模方向的近竖直平面数），以及 `SKILL.md` 评审流程。

## 用法
```bash
pip install cadquery
python scripts/step_summary.py part.step --pull z --min-draft 1.0
```


