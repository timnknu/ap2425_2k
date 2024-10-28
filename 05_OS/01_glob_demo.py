import glob
import os

print(sorted([10, -1, 2, -5, 20], reverse=True))

for fname in glob.glob('*.txt'):
    print(fname, os.path.getctime(fname))