#!/usr/bin/env python3
"""Print the text of a PowerPoint deck slide by slide (read-only).

Used by the storyteller-critic to review a .pptx the user has edited.
Usage: python3 .claude/scripts/pptx_text.py paper/talks/<name>.pptx
Shows slide titles/body text, image counts, and speaker notes.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
REL = "{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"


def paragraphs(xml_bytes):
    root = ET.fromstring(xml_bytes)
    out = []
    for p in root.iter(f"{{{NS['a']}}}p"):
        t = "".join(x.text or "" for x in p.iter(f"{{{NS['a']}}}t")).strip()
        if t:
            out.append(t)
    return out


def main(path):
    with zipfile.ZipFile(path) as z:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        rels = ET.fromstring(z.read("ppt/_rels/presentation.xml.rels"))
        target = {r.get("Id"): r.get("Target") for r in rels.iter(REL)}
        ids = [s.get(f"{{{NS['r']}}}id") for s in pres.iter(f"{{{NS['p']}}}sldId")]
        for n, rid in enumerate(ids, 1):
            slide = "ppt/" + target[rid].lstrip("/").replace("ppt/", "")
            xml = z.read(slide)
            pics = len(re.findall(rb"<p:pic>", xml))
            print(f"--- Slide {n}" + (f"  [{pics} image(s)]" if pics else ""))
            for t in paragraphs(xml):
                print(f"  {t}")
            rel_path = slide.replace("slides/", "slides/_rels/") + ".rels"
            if rel_path in z.namelist():
                srels = ET.fromstring(z.read(rel_path))
                for r in srels.iter(REL):
                    if r.get("Type", "").endswith("/notesSlide"):
                        note = "ppt/" + r.get("Target").replace("../", "")
                        lines = [t for t in paragraphs(z.read(note)) if not t.isdigit()]
                        if lines:
                            print("  [notes] " + " / ".join(lines))
    print(f"\n{len(ids)} slides")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else sys.exit(__doc__))
