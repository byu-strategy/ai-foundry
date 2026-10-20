#!/usr/bin/env python3
"""Render ops/welcome-letter.md to a print-ready PDF via pandoc + WeasyPrint."""
import re, subprocess, sys, pathlib

HERE = pathlib.Path(__file__).parent
SRC, CSS = HERE / "welcome-letter.md", HERE / "welcome-letter.css"
OUT = HERE / "welcome-letter.pdf"

md = SRC.read_text()

# Strip the masthead and the signature table; both are rebuilt as styled HTML.
md = re.sub(r"^# .*?\n\n\*\*.*?\n\n---\n", "", md, count=1, flags=re.S)
md = re.sub(r"\n\|\s*\|\s*\|\n\|---\|---\|\n(?:\|.*\n)+", "\n", md)

# Indented "Label: https://..." continuation lines become styled reference spans.
def ref(m):
    return f'   [{m.group(1)}: [{m.group(2)}]({m.group(2)})]{{.ref}}\\'
md = re.sub(r"^   (\S[^:]*?): (https?://\S+)\s*$", ref, md, flags=re.M)
md = re.sub(r"\\\n\n", "\n\n", md)  # drop the break on the last ref of a group

# Break the line *before* a group of refs so the group starts on its own line.
def is_ref(t):
    return t.lstrip().startswith("[") and ".ref}" in t
lines = md.split("\n")
for i, line in enumerate(lines):
    if is_ref(line) and i and lines[i - 1].strip() and not is_ref(lines[i - 1]):
        lines[i - 1] += "\\"
md = "\n".join(lines)

body = subprocess.run(
    ["pandoc", "--from=markdown+bracketed_spans", "--to=html5"],
    input=md, text=True, capture_output=True, check=True).stdout

SIG_FIELDS = [("Student name (print)", ""), ("Signature", ""), ("Date", " short")]
sig = "\n".join(
    f'<div class="sig-row"><span class="sig-label">{l}</span>'
    f'<span class="sig-line{c}"></span></div>' for l, c in SIG_FIELDS)

html = f"""<!doctype html><html><head><meta charset="utf-8">
<title>Welcome to the AI Foundry</title></head><body>
<p class="kicker">BYU Marriott School of Business</p>
<h1>Welcome to the AI&nbsp;Foundry</h1>
<p class="subtitle">AI Foundry Lab &nbsp;·&nbsp; MBA 693R-011 &nbsp;/&nbsp; STRAT 490R-001</p>
<hr>
{body}
<div class="sig">{sig}</div>
</body></html>"""

tmp = HERE / ".welcome-letter.build.html"
tmp.write_text(html)
subprocess.run(["weasyprint", "-s", str(CSS), str(tmp), str(OUT)], check=True)
tmp.unlink()
print(f"wrote {OUT}")
