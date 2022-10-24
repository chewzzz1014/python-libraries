from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # send 200 OK response
        self.send_response(200)

        # send headers
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

        # response body
        # wfile: writeable file
        # enocde string into byte object
        self.wfile.write("hello, http!\n".encode())


if __name__ == "__main__":
    server_address = ("", 8000) # serve on all addresses, port 8000
    httpd = HTTPServer(server_address, HelloHandler)

    # start handling HTTP requests
    httpd.serve_forever()