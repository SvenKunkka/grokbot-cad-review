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
