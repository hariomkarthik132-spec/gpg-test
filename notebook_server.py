#!/usr/bin/env python3
import http.server
import socketserver
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("0.0.0.0", port), handler) as httpd:
    print(f"Notebook-friendly server running: http://127.0.0.1:{port}")
    httpd.serve_forever()
