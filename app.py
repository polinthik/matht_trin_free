import http.server
import socketserver

PORT = 8000

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Открой в браузере: http://localhost:{PORT}")
    print("Остановить: Ctrl+C")
    httpd.serve_forever()
    