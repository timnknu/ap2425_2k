import glob
import os

all_files = []

for fname in glob.glob('*.txt'):
    timestamp = os.path.getctime(fname)
    d = (timestamp, fname)
    all_files.append(d)
print(all_files)

srt_list = sorted(all_files)
print(srt_list)

for ctime, fname in srt_list:
    print(ctime, fname)
    with open(fname) as fi:
        txt = fi.read()
    print('-----')
    print(txt)
    print('-----')
