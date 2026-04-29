# auto-md-convert

A Claude skill that automatically converts uploaded `.docx` and `.pdf` files to Markdown before reading them.

## Why?

When you upload a Word or PDF document, Claude normally reads the raw file. This skill converts it to clean Markdown first, which:

- **Saves tokens** — Markdown is more compact than raw document formats
- **Improves accuracy** — structured text is easier for Claude to interpret
- **Works transparently** — Claude converts silently and gets straight to your question

## What it does

When you upload a `.docx` or `.pdf` file, Claude will:

1. Convert it to Markdown using the included `convert.py` script
2. Read the Markdown instead of the raw file
3. Also save the `.md` file to outputs so you can download it if needed

## Supported formats

| Format | Library used |
|--------|-------------|
| `.docx` | `python-docx` |
| `.pdf` | `pymupdf` |

Dependencies are auto-installed if missing.

## When it does NOT trigger

- When you ask Claude to **edit** the original file (e.g. "add a table to this .docx") — use the `docx` or `pdf` skill instead
- When you need the exact original formatting/styling
- For scanned PDFs without a text layer (no OCR support)

## Installation

1. Download [`auto-md-convert.zip`](./auto-md-convert.zip)
2. Go to [claude.ai](https://claude.ai) → **Settings → Skills**
3. Upload the zip file

## Files

```
auto-md-convert/
├── SKILL.md       ← skill definition (read by Claude)
├── convert.py     ← conversion script
└── auto-md-convert.zip  ← ready-to-upload package
```

## License

MIT
