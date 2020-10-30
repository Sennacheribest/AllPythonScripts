fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print(f'File cannot be opened: {fname}')
    exit()

count = 0
total = 0
average = 0

for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    line = line.rstrip()
    count += 1
    ipos = line[(line.find(':')) + 1:]
    total = total + float(ipos)
    average = total / count

print(f'Average spam confidence: {average}')
