import glob
import os

all_files = []

for fname in glob.glob('*.txt'):
    timestamp = os.path.getctime(fname)
    d = (timestamp, fname)
    all_files.append(d)
print(all_files)

print((1, 2) < (-2, 4))
print((-2, 2) < (-2, 4))
print('abc' < '0bd')