import glob
import os

all_files = []

for fname in glob.glob('*.txt'):
    timestamp = os.path.getctime(fname)
    d = (timestamp, fname)
    all_files.append(d)
print(all_files)