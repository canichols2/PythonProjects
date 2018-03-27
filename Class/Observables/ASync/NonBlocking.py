import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import ThreadingMixIn

HandlerClass = SimpleHTTPRequestHandler


class ThreadedServer(ThreadingMixIn,BaseHTTPServer.HTTPServer):
    """Starts a webserver in a separate thread"""

ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ThreadedServer(server_address, HandlerClass)

# http://127.0.0.1:8000/

sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")


# Expected Result:
#  Will serve and allow the print messages 
#   after work as well.
httpd.serve_forever()

# Acutal Result:
#  They don't run. 
#  ServeForever still blocks the rest of the program
print("Test1")
print("Test1")
print("Test1")
print("Test1")
print("Test1")
print("Test1")
print("Test1")
