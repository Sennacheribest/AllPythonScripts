fhand = open("romeo.txt")
result = list()
for line in fhand:
    words = line.rstrip().split()
    for i in range(len(words)):
        if not words[i] in result:
            result.append(words[i])
result.sort()
print(result)
