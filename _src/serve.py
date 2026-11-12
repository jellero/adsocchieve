"""Anteprima locale con URL "puliti" come su GitHub Pages / Netlify.
Uso:  python _src/serve.py [porta]   poi apri http://localhost:8000"""
import http.server, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def send_head(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]
        target = ROOT / path.lstrip("/")
        if not target.exists() and (ROOT / (path.strip("/") + ".html")).exists():
            self.path = path.rstrip("/") + ".html"
        elif not target.exists():
            self.send_response(404)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            body = (ROOT / "404.html").read_bytes()
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return None
        return super().send_head()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"http://localhost:{port}")
    http.server.ThreadingHTTPServer(("", port), Handler).serve_forever()
