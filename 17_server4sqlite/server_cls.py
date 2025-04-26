import wsgiref.simple_server
import traceback
import urllib

class WebInputEnvironmentServer:
    def __init__(self, handler_class):
        self.sessions = {}
        self.last_user_index = 0
        self.HandlerClass = handler_class

    def application(self, environ, start_response):
        http_status = '200 OK'
        resp_headers = [
            ('Content-Type', 'text/html')
        ]

        req = environ['QUERY_STRING']
        form_data = urllib.parse.parse_qs(req)
        try:
            cont_len_str = environ.get('CONTENT_LENGTH', '')
            if len(cont_len_str)>0:
                data_length = int(cont_len_str)
                f = environ['wsgi.input']
                post_data_str = f.read(data_length).decode('utf-8')
                post_data_dict = urllib.parse.parse_qs(post_data_str)
                form_data.update(post_data_dict)
        except:
            print(traceback.format_exc())
        #

        if environ['PATH_INFO'] == '/':
            # коли запит був на "головну сторінку"
            # Значить - це новий користувач
            self.last_user_index += 1
            uid = self.last_user_index
            self.sessions[uid] = self.HandlerClass(uid)
        else:
            # коли запит був від користувача, який уже починав взаємодіяти з цим сервером
            # Значить - це новий користувач, якого "ми вже бачили"
            addr_parts = environ['PATH_INFO'].split('/')
            try:
                uid = int(addr_parts[1])
            except:
                uid = None
        if uid in self.sessions:
            # це дійсно коректний ідентифікатор користувача
            resp_str, resp_headers, is_final = self.sessions[uid].handle(environ, form_data)
            if is_final:
                # якщо це остання відповідь, то видалимо сесію
                del self.sessions[uid]
        else:
            resp_headers = [
                ('Content-Type', 'text/plain; charset=utf-8'),
            ]
            resp_str = "ПОМИЛКА: Невідомий користувач"
        #
        start_response(http_status, resp_headers)

        resp_bytes = bytes(resp_str, encoding='utf-8')
        return [resp_bytes]

    def run(self):
        #--------------------------------------------------------------------
        # Блок 2
        HOST = ''                 # Комп'ютер для з'єднання
        PORT = 5556              # Порт для з'єднання

        wsgiref.simple_server.WSGIServer.allow_reuse_address = True
        wsgiref.simple_server.WSGIServer.allow_reuse_port = True
        srv = wsgiref.simple_server.WSGIServer((HOST, PORT), wsgiref.simple_server.WSGIRequestHandler)
        srv.set_app(self.application)

        # Блок 3
        try:
            srv.serve_forever()
        except:
            print('Exception occurred')
            print(traceback.format_exc())
        #
        srv.server_close()
    #
#


if __name__ == "__main__":
    from user_sessions import BaseHandler
    req_handler_class = BaseHandler
    s = WebInputEnvironmentServer(req_handler_class)
    s.run()