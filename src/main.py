import http.server
import socketserver
from http import HTTPStatus

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello test changed changed #5 01.23___ \n from 176.15.115.242')

httpd = socketserver.TCPServer(('', 5555), Handler)
httpd.serve_forever()
