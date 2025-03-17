import wsgiref.simple_server
import traceback

import openpyxl

def read_rates():
    rates = {}
    wb = openpyxl.load_workbook('rates-example.xlsx')
    ws = wb.worksheets[0]
    for r in ws.iter_rows(values_only=True):
        ccode1, ccode2, rate = r
        key = (ccode1, ccode2)
        rates[key] = rate
    return rates
#-----------------------------------------




# Блок 1
def application(environ, start_response):
    pass

#--------------------------------------------------------------------
# Блок 2
HOST = ''                 # Комп'ютер для з'єднання
PORT = 5556              # Порт для з'єднання

wsgiref.simple_server.WSGIServer.allow_reuse_address = True
wsgiref.simple_server.WSGIServer.allow_reuse_port = True
srv = wsgiref.simple_server.WSGIServer((HOST, PORT), wsgiref.simple_server.WSGIRequestHandler)
srv.set_app(application)


# Блок 3
try:
    srv.serve_forever()
except:
    print('Exception occurred')
    print(traceback.format_exc())
#
srv.server_close()