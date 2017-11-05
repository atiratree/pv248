from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse,parse_qs
from functools import reduce


class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200, 'OK')

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        parsed_url = urlparse(self.path)
        query_dict = parse_qs(parsed_url.query)
        query_view = reduce(lambda x, key: x + f'<li>{key}: {query_dict[key]}</li>', query_dict, '')

        # Send message back to client
        message = f'<h1>Hello world! called from {parsed_url.path}</h1>' + \
                  f'<ul>{query_view}</ul>'
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))