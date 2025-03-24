import json

with open('sample1.json', encoding='utf8') as f1:
    d = json.load(f1)
#print(d)
list_of_marks = []
for item in d['requests']:
    #print(item)
    #print(item['kv'])
    #print('---')
    list_of_marks.append(item['kv'])
print(list_of_marks)

import matplotlib.pyplot as plt
plt.hist(list_of_marks, bins=50)
plt.show()