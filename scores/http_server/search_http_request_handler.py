from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from http_server.settings import Settings
from http_server.utils import Utils
from http_server.view import View


class SearchHTTPRequestHandler(BaseHTTPRequestHandler):
    def set_content(self, query_dict):
        req_type = Utils.get_query_param(query_dict, Settings.F_KEY, Settings.HTML)
        req_query = Utils.get_query_param(query_dict, Settings.Q_KEY, '')

        if req_type == Settings.JSON:
            content_type = 'application/json'
            result = View.generate_json(req_query)

        else:
            content_type = 'text/html'
            result = View.generate_html_view(req_query)

        self.send_header('Content-type', content_type)
        self.end_headers()

        self.wfile.write(bytes(result, "utf8"))

    def do_POST(self):
        self.send_response(200, 'OK')
        parsed_url = urlparse(self.path)
        query_dict = parse_qs(parsed_url.query)
        self.set_content(query_dict)

    # GET
    def do_GET(self):
        self.send_response(200, 'OK')

        parsed_url = urlparse(self.path)
        query_dict = parse_qs(parsed_url.query)

        self.set_content(query_dict)
