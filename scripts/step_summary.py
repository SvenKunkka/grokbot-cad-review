#!/usr/bin/env python3
"""STEP 几何摘要 + 平面拔模角粗检（只读，不改模型）。"""
import argparse, json, math
import cadquery as cq

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("step")
    ap.add_argument("--pull", default="z", choices="xyz"); ap.add_argument("--min-draft", type=float, default=1.0)
    a = ap.parse_args()
    pull = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1)}[a.pull]
    shape = cq.importers.importStep(a.step).val()
    out = []
    for i, solid in enumerate(shape.Solids() or [shape]):
        bb = solid.BoundingBox(); low = 0; planes = 0
        for f in solid.Faces():
            if f.geomType() != "PLANE": continue
            planes += 1; n = f.normalAt()
            cosang = abs(n.x * pull[0] + n.y * pull[1] + n.z * pull[2])
            draft = math.degrees(math.asin(min(1.0, cosang)))
            if draft < a.min_draft and cosang < 0.999: low += 1
        out.append({"solid": i, "bbox_mm": [round(bb.xlen, 2), round(bb.ylen, 2), round(bb.zlen, 2)],
                    "volume_mm3": round(solid.Volume(), 1), "area_mm2": round(solid.Area(), 1),
                    "faces": len(solid.Faces()), "planar_faces": planes,
                    f"planar_faces_draft_lt_{a.min_draft}deg": low})
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
