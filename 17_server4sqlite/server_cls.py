import wsgiref.simple_server
import traceback
import urllib

class WebInputEnvironmentServer:
    def application(self, environ, start_response):
        http_status = '200 OK'
        resp_headers = [
            ('Content-Type', 'text/html')
        ]
        start_response(http_status, resp_headers)

        req = environ['QUERY_STRING']
        form_data = urllib.parse.parse_qs(req)
        try:
            cont_len_str = environ.get('CONTENT_LENGTH', '')
            if len(cont_len_str)>0:
                data_length = int(cont_len_str)
                f = environ['wsgi.input']
                post_data_str = f.read(data_length)
                post_data_dict = urllib.parse.parse_qs(post_data_str)
                form_data.update(post_data_dict)
        except:
            print(traceback.format_exc())
        #
        resp_str = str(form_data)

        if environ['PATH_INFO'] == '/':
            # коли запит був на "головну сторінку"
            pass
        else:
            # коли запит був від користувача, який уже починав взаємодіяти з цим сервером
            pass
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
    s = WebInputEnvironmentServer()
    s.run()