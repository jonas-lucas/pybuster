from http.server import HTTPServer, BaseHTTPRequestHandler


fake_routes = {
    "/": "<h1>Welcome to FakeCorp</h1><p>Nothing suspicious here.</p>",
    "/admin": "<h1>Admin Panel</h1><p>Access denied.</p>",
    "/login": "<form><input placeholder='user'></form>",
    "/robots.txt": "User-agent: *\nDisallow: /secret",
    "/.git/HEAD": "ref: refs/heads/main",
    "/backup.zip": "[FAKE BINARY ZIP CONTENT]",
    "/secret": "<h2>This shouldn't be here</h2>",
    "/hidden-panel": "<h2>Hidden Control Panel</h2>",
    "/api/v1/users": '{"users": [{"id":1,"name":"admin"}]}',
    "/notes.txt": "TODO: Delete old backups from /backup.zip"
}


class GoatHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in fake_routes:
            self.send_response(200)
            if self.path.endswith(".zip"):
                self.send_header("Content-Type", "application/zip")
            elif self.path.endswith(".txt"):
                self.send_header("Content-Type", "text/plain")
            elif self.path.endswith(".json") or self.path.startswith("/api/"):
                self.send_header("Content-Type", "application/json")
            else:
                self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(fake_routes[self.path].encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def main(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, GoatHandler)
    print(f"Goat web server running on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    main()
