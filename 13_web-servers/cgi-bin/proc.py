import os
import urllib.parse

#print('Content-type: text/plain')
print('Content-type: text/html')
print()
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<meta charset="utf8">')
print('</head>')
print('<body>')
print('Hello world')
for i in range(10):
    print(i, i**2, '<br>')
print('<hr>')

req = os.environ['QUERY_STRING']
form_data = urllib.parse.parse_qs(req)
print(form_data)
print('</body>')
print('</html>')