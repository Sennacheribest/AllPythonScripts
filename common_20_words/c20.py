fname = input("Enter file: ")
fhand = open(fname)

counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

"""lst = list()
for key, value in counts.items():
    tmp = (value, key)
    lst.append(tmp)"""

lst = sorted([ (value, key) for key, value in counts.items() ], reverse=True)

for value, key in lst[:20]:
    print(key, value)
