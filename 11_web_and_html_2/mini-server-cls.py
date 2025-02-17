import socketserver

#--------------------------------------------------------------------
# Блок 2
class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print('connected from', self.client_address)
        request_lines = []
        while True:
            data = self.rfile.readline()
            line = str(data, encoding = 'utf-8')
            if len(line.rstrip()) == 0: # перевірити, чи складається рядок тільки з символів кінця рядка (\r, \n)
                break
            request_lines.append(line)
        #
        print('Request lines', request_lines)

        method, pth, proto = request_lines[0].split()
        if pth == '/':
            resp_str = "HTTP/1.1 200 OK\n"
            resp_str = resp_str + "Content-Type: text/html\n"
            resp_str = resp_str + "\n"
            resp_str = resp_str + "This is main page!\n\n"
            self.wfile.write(bytes(resp_str, encoding='utf-8')) # перетворити рядок у байти та відправити клієнту (або можна було так: self.wfile.write(resp_str.encode('utf-8')) )
        elif pth == '/about':
            resp_str = "HTTP/1.1 200 OK\n"
            resp_str = resp_str + "Content-Type: text/plain\n"
            resp_str = resp_str + "\n"
            resp_str = resp_str + "This is a second piece of information, and it is not an HTML\n\n"
            self.wfile.write(bytes(resp_str, encoding='utf-8'))

#--------------------------------------------------------------------
# Блок 3
HOST = ''                 # Комп'ютер для з'єднання
PORT = 5556              # Порт для з'єднання

srv = socketserver.ThreadingTCPServer((HOST, PORT), RequestHandler)
socketserver.ThreadingTCPServer.allow_reuse_address = True
socketserver.ThreadingTCPServer.allow_reuse_port = True

try:
    srv.serve_forever()
except:
    print('Exception occurred')
#
srv.server_close()