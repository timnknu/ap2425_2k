import http.server

# Блок 1
RequestHandler = http.server.CGIHTTPRequestHandler

#--------------------------------------------------------------------
# Блок 2
HOST = ''                 # Комп'ютер для з'єднання
PORT = 5556              # Порт для з'єднання

http.server.ThreadingHTTPServer.allow_reuse_address = True
http.server.ThreadingHTTPServer.allow_reuse_port = True
srv = http.server.ThreadingHTTPServer((HOST, PORT), RequestHandler)

# Блок 3
try:
    srv.serve_forever()
except:
    print('Exception occurred')
#
srv.server_close()