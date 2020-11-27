fname = input("Enter a file: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)

counts = dict()
for line in fhand:
    if line.startswith("From "): 
        line = line.rstrip()
        words = line.split()
        pieces = words[5].split(":")[0]
        # idiom: retrieve, create, and update counter
        counts[pieces] = counts.get(pieces, 0) + 1

lst = list()       
lst = sorted([ (key, value) for key, value in counts.items() ])

for k, v in lst:
    print(k, v)
