from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Send headers that instruct browsers not to cache any files
        # self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        # self.send_header("Pragma", "no-cache")
        # self.send_header("Expires", "0")
        self.send_header("Cache-Control", "must-revalidate")
        super().end_headers()

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            custom_404 = Path("404.html")
            if custom_404.exists():
                content = custom_404.read_bytes()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        super().send_error(code, message, explain)

def run_server(host="127.0.0.1", port=8000):
    server = ThreadingHTTPServer((host, port), CustomHandler)
    print(f"Serving HTTP on {host}:{port} (http://{host}:{port}/) ...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped gracefully.")
        server.server_close()

if __name__ == "__main__":
    run_server()