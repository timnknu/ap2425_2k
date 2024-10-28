import glob
import os
import datetime

all_files = []

for fname in glob.glob('*.txt'):
    timestamp = os.path.getctime(fname)
    d = (timestamp, fname)
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
