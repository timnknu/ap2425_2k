import docx

d = docx.Document("file01.docx")
for p in d.paragraphs:
    print('-----new paragraph-----')
    for tr in p.runs:
        print(tr.text, ':', tr.font.color.type)
