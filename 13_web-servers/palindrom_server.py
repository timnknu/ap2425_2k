import http.server

# Блок 2
RequestHandler = http.server.CGIHTTPRequestHandler

#--------------------------------------------------------------------
# Блок 3
HOST = ''                 # Комп'ютер для з'єднання
PORT = 5556              # Порт для з'єднання

http.server.ThreadingHTTPServer.allow_reuse_address = True
http.server.ThreadingHTTPServer.allow_reuse_port = True
srv = http.server.ThreadingHTTPServer((HOST, PORT), RequestHandler)

try:
    srv.serve_forever()
except:
    print('Exception occurred')
#
srv.server_close()