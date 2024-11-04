import zipfile
import re
import sys
print(sys.argv)

P = sys.argv[1]
#P = input() # and command line < redirect

#P = "import\s.*"
# Знайти файли, які містять тест,
# що відповідає заданому регулярному виразу.
#  Вивести імена знайдених файлів та
#  знайдений текст

with zipfile.ZipFile('../my-arch.zip') as zf:
    #print(zf.namelist())
    for item in zf.infolist():
        with zf.open(item) as cf:
            content = cf.read()
            s = content.decode('utf-8')
            fnd = re.findall(P, s)
            if len(fnd)>0:
                print('Found in', item.filename)
                for substr in fnd:
                    print(substr)
                print('----')

