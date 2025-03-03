import urllib.parse
s = 'http://localhost:5556/myprog?var=%D0%BF%D1%80%D0%B8%D0%B2%D1%96%D1%82%2C+%D1%81%D0%B2%D1%96%D1%82&parol=mybigsecret&var=123'

uri_parts = urllib.parse.urlparse(s)

#print(uri_parts.query)

d = urllib.parse.parse_qs(uri_parts.query)
print(d)
