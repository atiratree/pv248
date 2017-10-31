from http.server import BaseHTTPRequestHandler


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200, 'OK')

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "<h1>Hello world!</h1"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))