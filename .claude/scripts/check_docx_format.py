#!/usr/bin/env python3
"""APA 7 format checks on a Word manuscript (.docx), read-only.

Used by the writer-critic and verifier. Never modifies the file.

Usage:
    python3 .claude/scripts/check_docx_format.py paper/manuscript.docx [--abstract-limit 250]

Checks: page size and margins, body font and size, double spacing, running
head and page number, Abstract and Keywords, APA Level 1 headings
(no "Introduction" heading; Method/Results/Discussion present), References
with hanging indents, Table/Figure numbering and in-text callouts, no
vertical table borders, and common APA statistics errors.
Exit code 1 if any FAIL.
"""
import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
APA_FONTS = {  # font -> acceptable size in half-points (APA 7 §2.19)
    "Times New Roman": 24, "Calibri": 22, "Arial": 22, "Georgia": 22,
    "Lucida Sans Unicode": 20, "Computer Modern": 20,
}

results = []


def report(status, check, detail=""):
    results.append((status, check, detail))


def attr(el, name):
    return None if el is None else el.get(W + name)


def para_text(p):
    return "".join(t.text or "" for t in p.iter(W + "t"))


def style_props(styles, sid, seen=None):
    """Resolve font, size, line spacing, indents through basedOn chains."""
    seen = seen or set()
    out = {}
    st = styles.get(sid)
    if st is None or sid in seen:
        return out
    seen.add(sid)
    based = st.find(W + "basedOn")
    if based is not None:
        out.update(style_props(styles, attr(based, "val"), seen))
    rpr, ppr = st.find(W + "rPr"), st.find(W + "pPr")
    if rpr is not None:
        f, sz = rpr.find(W + "rFonts"), rpr.find(W + "sz")
        if f is not None and attr(f, "ascii"):
            out["font"] = attr(f, "ascii")
        if sz is not None:
            out["size"] = int(attr(sz, "val"))
    if ppr is not None:
        sp, ind, jc = ppr.find(W + "spacing"), ppr.find(W + "ind"), ppr.find(W + "jc")
        if sp is not None and attr(sp, "line"):
            out["line"] = int(attr(sp, "line"))
        if ind is not None:
            for k in ("firstLine", "hanging", "left"):
                if attr(ind, k) is not None:
                    out[k] = int(attr(ind, k))
        if jc is not None:
            out["jc"] = attr(jc, "val")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--abstract-limit", type=int, default=250)
    a = ap.parse_args()

    with zipfile.ZipFile(a.docx) as z:
        doc = ET.fromstring(z.read("word/document.xml"))
        styles_xml = ET.fromstring(z.read("word/styles.xml"))
        headers = [z.read(n).decode("utf-8") for n in z.namelist() if re.match(r"word/header\d*\.xml", n)]

    styles = {attr(s, "styleId"): s for s in styles_xml.iter(W + "style")}
    names = {attr(s, "styleId"): attr(s.find(W + "name"), "val") for s in styles_xml.iter(W + "style")}
    defaults = {}
    dd = styles_xml.find(W + "docDefaults")
    if dd is not None:
        f, sz, sp = dd.find(f".//{W}rFonts"), dd.find(f".//{W}sz"), dd.find(f".//{W}spacing")
        defaults = {"font": attr(f, "ascii"), "size": int(attr(sz, "val")) if sz is not None else None,
                    "line": int(attr(sp, "line")) if sp is not None and attr(sp, "line") else None}

    # ---- Page setup -----------------------------------------------------------
    sect = doc.find(f".//{W}body/{W}sectPr")
    pgmar, pgsz = (sect.find(W + "pgMar"), sect.find(W + "pgSz")) if sect is not None else (None, None)
    if pgmar is None:
        report("FAIL", "Margins", "no page margins found")
    else:
        m = {k: int(attr(pgmar, k)) for k in ("top", "bottom", "left", "right")}
        ok = all(abs(v - 1440) <= 20 for v in m.values())
        report("PASS" if ok else "FAIL", "Margins 1 in", ", ".join(f"{k}={v / 1440:.2f}in" for k, v in m.items()))
    if pgsz is not None:
        w, h = int(attr(pgsz, "w")), int(attr(pgsz, "h"))
        report("PASS" if (w, h) in ((12240, 15840), (11906, 16838)) else "WARN", "Page size",
               f"{w / 1440:.2f} x {h / 1440:.2f} in")

    # ---- Font and spacing -----------------------------------------------------
    body = {**defaults, **style_props(styles, "Normal"), **style_props(styles, "BodyText")}
    font, size = body.get("font"), body.get("size")
    if font in APA_FONTS and size == APA_FONTS[font]:
        report("PASS", "Body font", f"{font} {size / 2:g} pt")
    else:
        report("WARN", "Body font", f"{font} {size / 2 if size else '?'} pt -- APA 7 accepts e.g. Times New Roman 12, Calibri/Arial/Georgia 11")
    report("PASS" if body.get("line") == 480 else "FAIL", "Double spacing (body)", f"line={body.get('line')}")
    report("PASS" if body.get("firstLine") == 720 else "WARN", "First-line indent 0.5 in", f"firstLine={body.get('firstLine')}")

    # ---- Header -----------------------------------------------------------------
    hdr = " ".join(headers)
    has_page = "PAGE" in hdr
    head_text = re.sub(r"\s+", " ", " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", hdr))).strip()
    head_text = re.sub(r"\s*\d+$", "", head_text)
    report("PASS" if has_page else "FAIL", "Page number in header", "")
    if not head_text or head_text == "RUNNING HEAD":
        report("WARN", "Running head", "missing or still the placeholder (required for professional papers unless the journal says otherwise)")
    else:
        report("PASS" if len(head_text) <= 50 and head_text == head_text.upper() else "WARN",
               "Running head", f'"{head_text}" ({len(head_text)} chars; all caps, <= 50)')

    # ---- Paragraph walk ---------------------------------------------------------------
    paras = []
    for p in doc.iter(W + "p"):
        ps = p.find(f"{W}pPr/{W}pStyle")
        sid = attr(ps, "val") or "Normal"
        paras.append((sid, (names.get(sid) or sid).lower(), para_text(p).strip()))
    text_all = "\n".join(t for _, _, t in paras)

    h1 = [t for sid, n, t in paras if n == "heading 1" and t]
    lower_h1 = [t.lower() for t in h1]
    if "introduction" in lower_h1:
        report("FAIL", "No Introduction heading", "APA introductions have no heading")
    else:
        report("PASS", "No Introduction heading", "")
    for need in ("method", "results", "discussion"):
        present = any(t == need or t.startswith(need) or t.endswith(need) or "general discussion" in t for t in lower_h1)
        if need == "method":
            present = present or any(t.startswith("study") for t in lower_h1)
        report("PASS" if present else "FAIL", f"Level 1 heading: {need.title()}", "")
    report("PASS" if "references" in lower_h1 else "FAIL", "References heading", "")

    # Abstract and keywords
    idx = next((i for i, (_, _, t) in enumerate(paras) if t.lower() == "abstract"), None)
    if idx is None:
        report("FAIL", "Abstract", "no 'Abstract' label found")
    else:
        words, j = 0, idx + 1
        while j < len(paras) and not paras[j][2].lower().startswith("keywords"):
            if paras[j][1].startswith("heading") or paras[j][1] == "title":
                break
            words += len(paras[j][2].split())
            j += 1
        report("PASS" if words <= a.abstract_limit else "FAIL", "Abstract length", f"{words} words (limit {a.abstract_limit})")
    kw = next((t for _, _, t in paras if t.lower().startswith("keywords:")), None)
    if kw:
        n_kw = len([k for k in kw.split(":", 1)[1].split(",") if k.strip()])
        report("PASS" if 3 <= n_kw <= 5 else "WARN", "Keywords", f"{n_kw} keywords")
    else:
        report("FAIL", "Keywords", "no 'Keywords:' line")
    if re.search(r"\bJEL\b", text_all):
        report("FAIL", "No JEL codes", "JEL codes found")

    # References hanging indent
    bib = style_props(styles, "Bibliography")
    report("PASS" if bib.get("hanging") == 720 else "WARN", "Reference hanging indent", f"hanging={bib.get('hanging')}")

    # Table and figure labels and callouts
    for label in ("Table", "Figure"):
        nums = [int(m.group(1)) for _, n, t in paras
                for m in [re.fullmatch(rf"{label} (\d+)", t)] if m]
        if not nums:
            continue
        seq_ok = nums == list(range(1, len(nums) + 1))
        report("PASS" if seq_ok else "FAIL", f"{label} numbering", f"{label.lower()}s numbered {nums}")
        body_text = "\n".join(t for _, n, t in paras if not re.fullmatch(rf"{label} \d+", t))
        uncalled = [k for k in nums if not re.search(rf"\b{label}s? {k}\b|\b{label}s \d+(?:[,–-]| and )\s*{k}\b", body_text)]
        report("PASS" if not uncalled else "FAIL", f"{label} callouts in text",
               "all called out" if not uncalled else f"not mentioned in text: {uncalled}")

    # Vertical borders in tables
    vert = 0
    for tag in ("left", "right", "insideV", "start", "end"):
        for b in doc.iter(W + tag):
            if attr(b, "val") not in (None, "nil", "none"):
                vert += 1
    report("PASS" if vert == 0 else "FAIL", "No vertical table rules", f"{vert} vertical border(s)")

    # Statistics (INV-4)
    stats_issues = []
    for pat, msg in [(r"\bp\s*[=<>]\s*0\.\d", "leading zero on p"),
                     (r"\bp\s*=\s*\.?0?\.000\b", "p = .000"),
                     (r"\bn\.s\.", "'n.s.' instead of exact p"),
                     (r"\br\s*=\s*-?0\.\d", "leading zero on r")]:
        hits = re.findall(pat, text_all)
        if hits:
            stats_issues.append(f"{msg} ({len(hits)})")
    report("PASS" if not stats_issues else "WARN", "APA statistics", "; ".join(stats_issues) or "no common errors found")

    width = max(len(c) for _, c, _ in results)
    for status, check, detail in results:
        print(f"[{status:4}] {check:<{width}}  {detail}")
    fails = sum(s == "FAIL" for s, _, _ in results)
    print(f"\n{fails} FAIL, {sum(s == 'WARN' for s, _, _ in results)} WARN, {sum(s == 'PASS' for s, _, _ in results)} PASS")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
