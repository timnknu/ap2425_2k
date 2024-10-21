import re

inpstr = 'nnn 5 hello 1257 world 32'
# see also: https://regex101.com/
R_PATT = r'\d+'
print( re.findall(R_PATT, inpstr) )