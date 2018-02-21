#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from optparse import OptionParser

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        request_headers = self.headers
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("<html><head><title> web testing.</title></head>")
        self.wfile.write("<body><p>testing webpage.</p>")
        self.wfile.write("<p>Your headers: %s" % self.headers)
        self.wfile.write("<p>Source address: %s" % self.client_address[0])
        self.wfile.write("</body></html>")
        
def main():
    port = 8080
    print('Listening on localhost:%s' % port)
    server = HTTPServer(('', port), RequestHandler)
    server.serve_forever()

        
if __name__ == "__main__":
    parser = OptionParser()
    parser.usage = ("http-server that will display request paramaters \n"
                    "Run:\n\n"
                    "   reflect")
    (options, args) = parser.parse_args()
    
    main()
