# app/main.py
from http.server import SimpleHTTPRequestHandler, HTTPServer

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Dockerized Python App on EC2!")

if __name__ == "__main__":
    server = HTTPServer(("", 8000), Handler)
    print("Server running on port 8000...")
    server.serve_forever()
