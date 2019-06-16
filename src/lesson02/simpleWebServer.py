from http.server import *

class SimpleWebServer:
    def serve(self, port, getHandler):
        try:
            class MyHandler(BaseHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html; charset=UTF-8')
                    self.end_headers()
                    # Send the html message
                    self.wfile.write(getHandler(self.path).encode("UTF-8"))

            server = HTTPServer(('', port), MyHandler)
            print('Started web server on port ', port)

            server.serve_forever()

        except KeyboardInterrupt:
            print('^C received, shutting down the web server')
            server.socket.close()
