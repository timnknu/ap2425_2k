import os
import urllib.parse

print('Content-type: text/html')   # або 'text/plain'
print()
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<meta charset="utf8">')
print('</head>')
print('<body>')

req = os.environ['QUERY_STRING']
form_data = urllib.parse.parse_qs(req)
values_list = form_data['inp1']
#print('Ви ввели:', values_list[0])
txt = values_list[0]
if txt == txt[::-1]:
    print(f'Це паліндром: <pre>{txt}</pre>')
else:
    print(f'Це <b>не</b> є паліндромом: <pre>{txt}</pre>')

print('</body>')
print('</html>')