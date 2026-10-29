"""Inline assets/ images into src/deck.html and write a single offline index.html."""
import base64, mimetypes, pathlib, re

root = pathlib.Path(__file__).parent
html = (root / "src/deck.html").read_text()

def inline(match):
    path = root / "assets" / match.group(1)
    mime = mimetypes.guess_type(path.name)[0]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

out = root / "index.html"
out.write_text(re.sub(r"\{\{img:([^}]+)\}\}", inline, html))
print(out, out.stat().st_size)
