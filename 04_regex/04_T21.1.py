import re

R_PATT_SL = r'\d{4}/\d{1,2}/\d{1,2}'


with open('dates_inp1.txt', encoding='utf-8') as f:
    content = f.read()
    s = re.sub(R_PATT_SL, '!!!!!!!', content)
    print(s)