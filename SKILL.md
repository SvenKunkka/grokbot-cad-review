---
name: step-structure-review
description: 拿到 STEP/STP 结构图档需要做开模前或结构评审时使用；先取几何证据，再按清单出评审报告。
---
# 步骤
1. 运行 `scripts/step_summary.py <文件> --pull <开模方向>` 取尺寸、体积、拔模角粗检。
2. 需要壁厚 / 倒扣精确结果时用 Palmetto 或 augura。
3. 对照评审清单：壁厚均匀、拔模、加强筋 / 螺柱比例、倒扣与滑块、公差配合、装配干涉。
4. 每条问题写：位置证据、风险等级、建议修改、待确认项。
5. 输出可编辑报告（Markdown 或 DOCX），不改动原始图档。
