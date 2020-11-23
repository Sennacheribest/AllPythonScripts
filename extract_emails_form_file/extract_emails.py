fhand = open("mbox-short.txt")
count = 0

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or not line.startswith("From: "):
        continue
    count += 1
    print(words[1])
    
print("There were {} lines in the file with From as the first word".format(count))
