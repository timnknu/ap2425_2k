import re
import docx

#P1 = r'\d+'
P1 = r'укр'

d = docx.Document("file01.docx")
for p in d.paragraphs:
    for tr in p.runs:
        modified = re.sub(P1, 'REPLACED', tr.text)
        tr.text = modified

d.save("mod01.docx")
