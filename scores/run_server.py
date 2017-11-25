from http.server import HTTPServer
from http_server.search_http_request_handler import SearchHTTPRequestHandler


def run(server_class=HTTPServer, handler_class=SearchHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
