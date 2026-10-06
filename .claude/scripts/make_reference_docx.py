#!/usr/bin/env python3
"""Build the APA 7 Word style template used by pandoc (paper/word/apa7-reference.docx).

Starts from pandoc's default reference.docx and replaces its styles with APA 7
manuscript styles: Times New Roman 12 pt, double spacing, 0.5 in first-line
indents, 1 in margins, APA heading levels 1-5, hanging-indent references, and a
header with a running-head placeholder ("RUNNING HEAD") plus a page number.

Usage (from the project root):
    python3 .claude/scripts/make_reference_docx.py [output.docx]
    python3 .claude/scripts/make_reference_docx.py --letter paper/word/letter-reference.docx

--letter builds the variant used for response-to-reviewers and cover letters:
single spacing, a blank line between paragraphs, no first-line indent, and a
page number only (no running head).

Requires pandoc on PATH. Re-run after editing the STYLES table below. To use a
different APA-approved font (e.g., Calibri 11), change FONT and SIZE.
"""
import pathlib
import re
import subprocess
import sys
import tempfile
import zipfile

LETTER = "--letter" in sys.argv
ARGS = [a for a in sys.argv[1:] if a != "--letter"]

FONT = "Times New Roman"
SIZE = 24                            # half-points: 24 = 12 pt
DOUBLE = 240 if LETTER else 480      # line spacing in 240ths of a line: 480 = double
INDENT = 0 if LETTER else 720        # first-line indent in twips: 720 = 0.5 in
AFTER = 240 if LETTER else 0         # space after paragraphs (letters: one blank line)
HANG = 720                           # hanging indent for references

OUT = pathlib.Path(ARGS[0] if ARGS else
                   ("paper/word/letter-reference.docx" if LETTER else "paper/word/apa7-reference.docx"))


def ppr(align=None, first=None, left=None, hanging=None, line=DOUBLE,
        keep_next=False, outline=None, page_break_before=False):
    parts = []
    if keep_next:
        parts.append("<w:keepNext/>")
    if page_break_before:
        parts.append("<w:pageBreakBefore/>")
    parts.append(f'<w:spacing w:before="0" w:after="{AFTER}" w:line="{line}" w:lineRule="auto"/>')
    ind = []
    if left is not None:
        ind.append(f'w:left="{left}"')
    if first is not None:
        ind.append(f'w:firstLine="{first}"')
    if hanging is not None:
        ind.append(f'w:hanging="{hanging}"')
    parts.append(f"<w:ind {' '.join(ind)}/>" if ind else '<w:ind w:left="0" w:firstLine="0"/>')
    if align:
        parts.append(f'<w:jc w:val="{align}"/>')
    if outline is not None:
        parts.append(f'<w:outlineLvl w:val="{outline}"/>')
    return "<w:pPr>" + "".join(parts) + "</w:pPr>"


def rpr(bold=False, italic=False, size=SIZE, color=None, underline=False):
    parts = [f'<w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:eastAsia="{FONT}" w:cs="{FONT}"/>']
    if bold:
        parts.append("<w:b/><w:bCs/>")
    else:
        parts.append('<w:b w:val="0"/><w:bCs w:val="0"/>')
    if italic:
        parts.append("<w:i/><w:iCs/>")
    else:
        parts.append('<w:i w:val="0"/><w:iCs w:val="0"/>')
    parts.append(f'<w:color w:val="{color or "000000"}"/>')
    if underline:
        parts.append('<w:u w:val="single"/>')
    parts.append(f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>')
    return "<w:rPr>" + "".join(parts) + "</w:rPr>"


def pstyle(sid, name, p, r, based="Normal", nxt="BodyText", default=False):
    d = ' w:default="1"' if default else ""
    based_xml = f'<w:basedOn w:val="{based}"/>' if based else ""
    return (f'<w:style w:type="paragraph"{d} w:styleId="{sid}"><w:name w:val="{name}"/>'
            f'{based_xml}<w:next w:val="{nxt}"/><w:qFormat/>{p}{r}</w:style>')


def cstyle(sid, name, r, based="DefaultParagraphFont"):
    return (f'<w:style w:type="character" w:styleId="{sid}"><w:name w:val="{name}"/>'
            f'<w:basedOn w:val="{based}"/>{r}</w:style>')


# Paragraph styles: styleId -> (display name, pPr, rPr, nextStyle)
STYLES = {
    "Normal": ("Normal", ppr(), rpr(), "Normal"),
    "BodyText": ("Body Text", ppr(first=INDENT), rpr(), "BodyText"),
    "FirstParagraph": ("First Paragraph", ppr(first=INDENT), rpr(), "BodyText"),
    "Compact": ("Compact", ppr(), rpr(), "Compact"),
    # Title page
    "Title": ("Title", ppr(align="center", keep_next=True), rpr(bold=True), "Author"),
    "Subtitle": ("Subtitle", ppr(align="center"), rpr(bold=True), "Author"),
    "Author": ("Author", ppr(align="center"), rpr(), "Author"),
    "Date": ("Date", ppr(align="center"), rpr(), "BodyText"),
    "TitlePageLabel": ("Title Page Label", ppr(align="center", keep_next=True), rpr(bold=True), "BodyText"),
    # Abstract
    "AbstractTitle": ("Abstract Title", ppr(align="center", keep_next=True), rpr(bold=True), "Abstract"),
    "Abstract": ("Abstract", ppr(), rpr(), "Keywords"),
    "Keywords": ("Keywords", ppr(first=INDENT), rpr(), "BodyText"),
    # APA heading levels (Level 4/5 are run-in in APA; Word styles approximate them
    # as indented bold / bold italic paragraphs)
    "Heading1": ("heading 1", ppr(align="center", keep_next=True, outline=0), rpr(bold=True), "BodyText"),
    "Heading2": ("heading 2", ppr(keep_next=True, outline=1), rpr(bold=True), "BodyText"),
    "Heading3": ("heading 3", ppr(keep_next=True, outline=2), rpr(bold=True, italic=True), "BodyText"),
    "Heading4": ("heading 4", ppr(first=INDENT, keep_next=True, outline=3), rpr(bold=True), "BodyText"),
    "Heading5": ("heading 5", ppr(first=INDENT, keep_next=True, outline=4), rpr(bold=True, italic=True), "BodyText"),
    # References
    "Bibliography": ("Bibliography", ppr(left=HANG, hanging=HANG), rpr(), "Bibliography"),
    # Response letters: reviewer comments set off from responses
    "RefereeComment": ("Referee Comment", ppr(left=720), rpr(italic=True), "BodyText"),
    # Tables and figures (APA: number bold, title italic, both above; note below)
    "TableNumber": ("Table Number", ppr(keep_next=True, page_break_before=True), rpr(bold=True), "TableTitle"),
    "TableTitle": ("Table Title", ppr(keep_next=True), rpr(italic=True), "BodyText"),
    "TableNote": ("Table Note", ppr(), rpr(), "BodyText"),
    "FigureNumber": ("Figure Number", ppr(keep_next=True, page_break_before=True), rpr(bold=True), "FigureTitle"),
    "FigureTitle": ("Figure Title", ppr(keep_next=True), rpr(italic=True), "BodyText"),
    "FigureNote": ("Figure Note", ppr(), rpr(), "BodyText"),
    "TableCaption": ("Table Caption", ppr(keep_next=True), rpr(italic=True), "BodyText"),
    "ImageCaption": ("Image Caption", ppr(), rpr(), "BodyText"),
    "Caption": ("Caption", ppr(), rpr(italic=True), "BodyText"),
    "Figure": ("Figure", ppr(keep_next=True), rpr(), "BodyText"),
    "CaptionedFigure": ("Captioned Figure", ppr(keep_next=True), rpr(), "BodyText"),
    "BlockText": ("Block Text", ppr(left=720), rpr(), "BodyText"),
    "FootnoteText": ("footnote text", ppr(line=240, first=INDENT), rpr(size=20), "FootnoteText"),
}

TABLE_STYLE = (
    '<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table"/>'
    '<w:basedOn w:val="TableNormal"/><w:tblPr><w:tblStyleRowBandSize w:val="1"/>'
    '<w:tblStyleColBandSize w:val="1"/><w:tblBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
    '<w:left w:val="nil"/><w:right w:val="nil"/><w:insideH w:val="nil"/><w:insideV w:val="nil"/>'
    '</w:tblBorders></w:tblPr>'
    '<w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/></w:pPr>'
    '<w:tblStylePr w:type="firstRow"><w:tcPr><w:tcBorders>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/></w:tcBorders></w:tcPr></w:tblStylePr>'
    '</w:style>'
)

DOC_DEFAULTS = (
    "<w:docDefaults><w:rPrDefault>" + rpr()
    + '</w:rPrDefault><w:pPrDefault><w:pPr><w:spacing w:before="0" w:after="0" '
    f'w:line="{DOUBLE}" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
)

HEADER = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<w:hdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
    '<w:p><w:pPr><w:pStyle w:val="Header"/><w:tabs><w:tab w:val="right" w:pos="9360"/></w:tabs>'
    '<w:spacing w:line="240" w:lineRule="auto"/><w:ind w:firstLine="0"/></w:pPr>'
    + ("" if LETTER else f'<w:r>{rpr()}<w:t xml:space="preserve">RUNNING HEAD</w:t></w:r>') +
    f'<w:r>{rpr()}<w:tab/></w:r>'
    f'<w:r>{rpr()}<w:fldChar w:fldCharType="begin"/></w:r>'
    f'<w:r>{rpr()}<w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
    f'<w:r>{rpr()}<w:fldChar w:fldCharType="separate"/></w:r>'
    f'<w:r>{rpr()}<w:t>1</w:t></w:r>'
    f'<w:r>{rpr()}<w:fldChar w:fldCharType="end"/></w:r>'
    '</w:p></w:hdr>'
)

SECT_PR = (
    '<w:sectPr><w:headerReference w:type="default" r:id="rId9001"/>'
    '<w:pgSz w:w="12240" w:h="15840"/>'
    '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
    'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>'
)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        src = pathlib.Path(tmp) / "default.docx"
        subprocess.run(["pandoc", "-o", str(src), "--print-default-data-file", "reference.docx"], check=True)
        with zipfile.ZipFile(src) as z:
            files = {n: z.read(n) for n in z.namelist()}

    styles = files["word/styles.xml"].decode("utf-8")
    styles = re.sub(r"<w:docDefaults>.*?</w:docDefaults>", DOC_DEFAULTS, styles, flags=re.S)
    for sid, (name, p, r, nxt) in STYLES.items():
        new = pstyle(sid, name, p, r, based=None if sid == "Normal" else "Normal",
                     nxt=nxt, default=(sid == "Normal"))
        pat = re.compile(rf'<w:style w:type="paragraph"[^>]*w:styleId="{sid}".*?</w:style>', re.S)
        styles, n = pat.subn(new.replace("\\", "\\\\"), styles, count=1)
        if n == 0:
            styles = styles.replace("</w:styles>", new + "</w:styles>")
    styles, n = re.subn(r'<w:style w:type="table"[^>]*w:styleId="Table".*?</w:style>', TABLE_STYLE, styles, count=1, flags=re.S)
    if n == 0:
        styles = styles.replace("</w:styles>", TABLE_STYLE + "</w:styles>")
    styles = re.sub(r'(<w:style w:type="character"[^>]*w:styleId="Hyperlink".*?)<w:color w:val="[0-9A-Fa-f]+"\s*/>',
                    r'\1<w:color w:val="000000"/>', styles, flags=re.S)
    files["word/styles.xml"] = styles.encode("utf-8")

    doc = files["word/document.xml"].decode("utf-8")
    if "<w:sectPr" in doc:
        doc = re.sub(r"<w:sectPr.*?</w:sectPr>|<w:sectPr[^>]*/>", SECT_PR, doc, count=1, flags=re.S)
    else:
        doc = doc.replace("</w:body>", SECT_PR + "</w:body>")
    files["word/document.xml"] = doc.encode("utf-8")

    files["word/header1.xml"] = HEADER.encode("utf-8")
    rels = files["word/_rels/document.xml.rels"].decode("utf-8")
    if "rId9001" not in rels:
        rels = rels.replace(
            "</Relationships>",
            '<Relationship Id="rId9001" '
            'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" '
            'Target="header1.xml"/></Relationships>')
    files["word/_rels/document.xml.rels"] = rels.encode("utf-8")
    ct = files["[Content_Types].xml"].decode("utf-8")
    if "header1.xml" not in ct:
        ct = ct.replace(
            "</Types>",
            '<Override PartName="/word/header1.xml" '
            'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/></Types>')
    files["[Content_Types].xml"] = ct.encode("utf-8")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    order = ["[Content_Types].xml"] + [n for n in files if n != "[Content_Types].xml"]
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for n in order:
            z.writestr(n, files[n])
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
