import re

R_PATT_SL = r'(\d{4})/(\d{1,2})/(\d{1,2})'

def myfunc(obj):
    print('THIS IS myfunc:', obj)
    print(obj.groups())
    print()
    print(obj.group(2))
    print(obj.group(3))
    #'end', 'endpos', 'expand',
    # 'group', 'groupdict', 'groups', 'lastgroup',
    # 'lastindex', 'pos', 're', 'regs',
    # 'span', 'start', 'string'
    day = int(obj.group(3))
    month = int(obj.group(2))
    year = obj.group(1)
    s = f"{day:02d}.{month:02d}.{year}"
    return s

with open('dates_inp1.txt', encoding='utf-8') as f:
    content = f.read()
    s = re.sub(R_PATT_SL, myfunc, content)
    print(s)