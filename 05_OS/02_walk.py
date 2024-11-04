import os
import datetime
import re
import sys; print(sys.path)

all_files = []

for item in os.walk('.'):
    dirpath, dirnames, filenames = item
    for fname in filenames:
        if re.match(r'.*\.txt', fname) is None:
            continue
        print(dirpath, fname)
        full_fname = os.path.join(dirpath,fname)


        timestamp = os.path.getctime(full_fname)
        d = (timestamp, full_fname)
        all_files.append(d)
print(all_files)

srt_list = sorted(all_files)
print(srt_list)

# із модуля datetime:
# https://docs.python.org/3/library/datetime.html
# datetime.datetime
# datetime.timedelta

for ctime, fname in srt_list:
    dtm = datetime.datetime.fromtimestamp(ctime)
    s = dtm.strftime('time is %H:%M:%S, day is %a, date is %d/%m-%Y')
    print(ctime, s, fname)
    with open(fname) as fi:
        txt = fi.read()
    print('-----')
    print(txt)
    print('-----')

