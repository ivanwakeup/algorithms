import json
from dataclasses import asdict
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from flashcards.store import Card, add_cards, delete_card, load_cards, set_current, update_card

INDEX_HTML = Path(__file__).parent / "static" / "index.html"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._send(200, "text/html; charset=utf-8", INDEX_HTML.read_bytes())
        elif self.path == "/api/cards":
            # read from disk on every request so cards added via the CLI show up on refresh
            body = json.dumps([asdict(c) for c in load_cards()]).encode()
            self._send(200, "application/json", body)
        else:
            self._send(404, "text/plain", b"not found")

    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        if self.path == "/api/current":
            # the page reports which card is on screen so Claude can look it up with `python -m flashcards current`
            set_current(data["id"])
            return self._send(204, "text/plain", b"")
        if self.path != "/api/cards":
            return self._send(404, "text/plain", b"not found")
        try:
            card = Card(question=data["question"], answer=data["answer"], category=data["category"].strip())
            added = add_cards([card])
        except (ValueError, KeyError, TypeError, AttributeError) as e:
            return self._send(400, "text/plain", str(e).encode())
        if not added:
            return self._send(409, "text/plain", b"a card with that question already exists")
        self._send(201, "application/json", json.dumps(asdict(card)).encode())

    def do_PUT(self):
        prefix = "/api/cards/"
        if not self.path.startswith(prefix):
            return self._send(404, "text/plain", b"not found")
        try:
            data = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
            card = update_card(self.path[len(prefix):], data["question"], data["answer"])
        except (ValueError, KeyError, TypeError) as e:
            return self._send(400, "text/plain", str(e).encode())
        if card is None:
            return self._send(404, "text/plain", b"not found")
        self._send(200, "application/json", json.dumps(asdict(card)).encode())

    def do_DELETE(self):
        prefix = "/api/cards/"
        if self.path.startswith(prefix) and delete_card(self.path[len(prefix):]):
            self._send(204, "text/plain", b"")
        else:
            self._send(404, "text/plain", b"not found")

    def _send(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")  # so a refresh always picks up UI changes
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


def serve(host="127.0.0.1", port=8765):
    with ThreadingHTTPServer((host, port), Handler) as httpd:
        print(f"flashcards running at http://{host}:{port}  (Ctrl-C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
