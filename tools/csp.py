#!/usr/bin/env python3
"""Recalcula la huella SHA-256 del <script> en línea y la escribe en la política CSP del HTML.

Uso:  python3 tools/csp.py index.html
Ejecútalo cada vez que cambies el JavaScript de la página: si la huella no coincide,
el navegador bloquea el script (en GitHub Pages) y la página no arranca.
"""
import base64, hashlib, re, sys
from pathlib import Path

def main(path: str) -> int:
    f = Path(path)
    html = f.read_text(encoding="utf-8")
    scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
    if len(scripts) != 1:
        print(f"Se esperaba 1 script en línea y hay {len(scripts)}.", file=sys.stderr)
        return 1
    digest = base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode()
    new, n = re.subn(r"'sha256-[A-Za-z0-9+/=]+'", f"'sha256-{digest}'", html, count=1)
    if n != 1:
        print("No encontré la huella 'sha256-…' en la meta Content-Security-Policy.", file=sys.stderr)
        return 1
    if new != html:
        f.write_text(new, encoding="utf-8")
    print(f"CSP actualizada: sha256-{digest}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "index.html"))
