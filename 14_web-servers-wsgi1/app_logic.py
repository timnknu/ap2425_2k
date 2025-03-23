import openpyxl
import urllib.parse

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
    http_status = '200 OK'
    resp_headers = [
        ('Content-Type', 'text/html')
    ]
    start_response(http_status, resp_headers)

    if environ['PATH_INFO'] == '/':
        with open('main-page.html', 'rb') as f:
            resp_bytes = f.read()
        return [resp_bytes]
    if environ['PATH_INFO'] == '/show-result':
        req = environ['QUERY_STRING']
        form_data = urllib.parse.parse_qs(req)
        values_list = form_data['amount']
        x = float(values_list[0])
        s = str(x*2)
        resp_str = f'<html><body><h1>x*2={s}</h1></body></html>'
        resp_bytes = bytes(resp_str, encoding='utf-8')
        return [resp_bytes]
    else:
        s = str(environ)
        resp_str = f'<html><body><h1>Another page</h1><br>{s}</body></html>'
        resp_bytes = bytes(resp_str, encoding='utf-8')
        return [resp_bytes]
