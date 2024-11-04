import zipfile

with zipfile.ZipFile('../my-arch.zip') as zf:
    #print(zf.namelist())
    for item in zf.infolist():
        with zf.open(item) as cf:
            content = cf.read()
            s = content.decode('utf-8')
            print('-'*80)
            print(item.filename)
            print(s)
            print('-'*80)
