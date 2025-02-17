import socketserver

#--------------------------------------------------------------------
# Блок 2
class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('connected from', self.client_address)
        while True:
            data = self.rfile.readline().strip()
            pal = str(data, encoding = 'utf-8')
            res = bytes(self._test_palindrome(pal)) + b'\n'
            self.wfile.write(res)
        print('disconnected', self.client_address)

#--------------------------------------------------------------------
# Блок 3
HOST = ''                 # Комп'ютер для з'єднання
PORT = 5556              # Порт для з'єднання

srv = socketserver.ThreadingTCPServer((HOST, PORT), RequestHandler)
socketserver.TCPServer.allow_reuse_address = True
socketserver.TCPServer.allow_reuse_port = True

try:
    srv.serve_forever()
except:
    print('Exception occurred')
#
srv.server_close()