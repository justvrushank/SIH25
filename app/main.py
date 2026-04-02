import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Tuple


def route(path: str) -> Tuple[int, dict[str, str]]:
    if path == "/health":
        return HTTPStatus.OK, {"status": "ok"}
    if path == "/":
        return HTTPStatus.OK, {
            "name": "SIH25 Service",
            "message": "Project bootstrap is complete and runnable.",
        }
    return HTTPStatus.NOT_FOUND, {"error": "not_found"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 (HTTP method name)
        status, payload = route(self.path)
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run(host: str = "0.0.0.0", port: int = 8000) -> None:
    server = HTTPServer((host, port), Handler)
    print(f"Serving on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
