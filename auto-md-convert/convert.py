#!/usr/bin/env python3
"""
auto-md-convert: converteert .docx en .pdf naar markdown.
Gebruik: python convert.py <pad-naar-bestand>
"""
import sys
import os
from pathlib import Path


def convert_docx(input_path: Path) -> str:
    """Converteer .docx naar markdown met behulp van python-docx."""
    try:
        from docx import Document
    except ImportError:
        os.system("pip install --break-system-packages python-docx -q")
        from docx import Document

    doc = Document(input_path)
    lines = []

    for element in doc.element.body:
        tag = element.tag.split("}")[-1]

        if tag == "p":
            # Paragraph
            from docx.text.paragraph import Paragraph
            para = Paragraph(element, doc)
            text = para.text.strip()
            if not text:
                lines.append("")
                continue

            style = para.style.name if para.style else ""
            if style.startswith("Heading 1") or style == "Title":
                lines.append(f"# {text}")
            elif style.startswith("Heading 2"):
                lines.append(f"## {text}")
            elif style.startswith("Heading 3"):
                lines.append(f"### {text}")
            elif style.startswith("Heading 4"):
                lines.append(f"#### {text}")
            elif style.startswith("Heading 5"):
                lines.append(f"##### {text}")
            elif style.startswith("Heading 6"):
                lines.append(f"###### {text}")
            elif style.startswith("List"):
                lines.append(f"- {text}")
            else:
                # Inline opmaak (bold/italic) per run
                parts = []
                for run in para.runs:
                    txt = run.text
                    if not txt:
                        continue
                    if run.bold and run.italic:
                        parts.append(f"***{txt}***")
                    elif run.bold:
                        parts.append(f"**{txt}**")
                    elif run.italic:
                        parts.append(f"*{txt}*")
                    else:
                        parts.append(txt)
                lines.append("".join(parts) if parts else text)

        elif tag == "tbl":
            # Tabel
            from docx.table import Table
            table = Table(element, doc)
            rows = []
            for row in table.rows:
                cells = [cell.text.strip().replace("\n", " ") for cell in row.cells]
                rows.append("| " + " | ".join(cells) + " |")
            if rows:
                # Header separator na eerste rij
                if len(rows) > 1:
                    sep = "| " + " | ".join(["---"] * len(table.rows[0].cells)) + " |"
                    rows.insert(1, sep)
                lines.append("")
                lines.extend(rows)
                lines.append("")

    return "\n".join(lines)


def convert_pdf(input_path: Path) -> str:
    """Converteer .pdf naar markdown met behulp van pymupdf."""
    try:
        import pymupdf
    except ImportError:
        os.system("pip install --break-system-packages pymupdf -q")
        import pymupdf

    doc = pymupdf.open(input_path)
    lines = [f"# {input_path.stem}", ""]

    for page_num, page in enumerate(doc, start=1):
        lines.append(f"## Pagina {page_num}")
        lines.append("")
        text = page.get_text("text")
        # Eenvoudige normalisatie: strip lege regels aan begin/eind
        text = text.strip()
        if text:
            lines.append(text)
        else:
            lines.append("_(geen tekst gevonden — mogelijk gescande pagina)_")
        lines.append("")

    doc.close()
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Gebruik: python convert.py <pad-naar-bestand>", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Bestand niet gevonden: {input_path}", file=sys.stderr)
        sys.exit(1)

    suffix = input_path.suffix.lower()
    if suffix == ".docx":
        markdown = convert_docx(input_path)
    elif suffix == ".pdf":
        markdown = convert_pdf(input_path)
    else:
        print(f"Niet ondersteund formaat: {suffix}", file=sys.stderr)
        sys.exit(1)

    # Schrijf naar /home/claude (voor Claude om te lezen)
    home_out = Path("/home/claude") / f"{input_path.stem}.md"
    home_out.write_text(markdown, encoding="utf-8")

    # Schrijf ook naar /mnt/user-data/outputs (voor de gebruiker)
    outputs_dir = Path("/mnt/user-data/outputs")
    outputs_dir.mkdir(parents=True, exist_ok=True)
    user_out = outputs_dir / f"{input_path.stem}.md"
    user_out.write_text(markdown, encoding="utf-8")

    # Stats
    original_size = input_path.stat().st_size
    md_size = len(markdown.encode("utf-8"))
    ratio = (md_size / original_size * 100) if original_size > 0 else 0

    print(f"✓ Geconverteerd: {input_path.name}")
    print(f"  Origineel: {original_size:,} bytes")
    print(f"  Markdown:  {md_size:,} bytes ({ratio:.0f}% van origineel)")
    print(f"  Gelezen:   {home_out}")
    print(f"  Download:  {user_out}")


if __name__ == "__main__":
    main()
