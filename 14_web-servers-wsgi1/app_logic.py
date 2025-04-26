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
        with open('main-page.html', 'r', encoding='utf8') as f:
            s = f.read()
        # Формуємо фрагмент для підстановки в "шаблон" головної html-сторінки зі словника, який повертає read_rates()
        d = read_rates()
        test_to_insert = ""
        for k, v in d.items():
            test_to_insert += f'<option value="{v}">{k[0]} - {k[1]}</option>\n'
        #
        resp_str = s.format(rate_info = test_to_insert)
        #resp_bytes = resp_str.encode()
        resp_bytes = bytes(resp_str, encoding='utf8')
        return [resp_bytes]
    if environ['PATH_INFO'] == '/show-result':
        req = environ['QUERY_STRING']
        form_data = urllib.parse.parse_qs(req)
        amount_list = form_data['amount']
        rates_list = form_data['rate']
        try:
            result = float(amount_list[0]) * float(rates_list[0])
            #text_to_insert = str(result)
            text_to_insert = f'{result:.2f}'
        except:
            text_to_insert = 'Сталася помилка :('
        #
        with open('response.html', 'r', encoding='utf8') as f:
            s = f.read()
        resp_str = s.format(result_field = text_to_insert)
        resp_bytes = bytes(resp_str, encoding='utf-8')
        return [resp_bytes]
    else:
        s = str(environ)
        resp_str = f'<html><body><h1>Another page</h1><br>{s}</body></html>'
        resp_bytes = bytes(resp_str, encoding='utf-8')
        return [resp_bytes]
