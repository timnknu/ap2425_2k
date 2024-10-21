import re

R_PATT = r'[.\-\w]+@[.\-\w]+'

with open('txt_doc.txt', encoding='utf-8') as f:
    content = f.read()
    fnd = re.findall(R_PATT, content)
    print(fnd)

# see also: https://regex101.com/library/6EL6YF
