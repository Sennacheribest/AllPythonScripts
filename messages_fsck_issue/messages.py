"""Python little snippet to parse /var/log/messages file from working linux server, 
   to extract information regarding fsck on root file system."""

"""import regular expression module."""   
import re

"""open required file. originally got it via this command-line:
   (# cat /var/log/messages > messages.txt)."""
file = open("messages.txt")

"""initialize some variables for later use."""
lst = list()
counts = dict()

"""read through file line by line."""
for line in file:
    """apply regular expression pattern to search then extract required piece of information."""
    stuff = re.findall("(^[a-zA-Z]+).*fsck-root.+", line)
    """get rid of any returend empty value."""
    if len(stuff) < 1: continue
    """looping through final list of cleaned data (stuff), then create a histogram of each value inside that list."""
    for item in stuff:
        """idiom: create, retrieve, and count frequincy of each item."""
        counts[item] = counts.get(item, 0) + 1
        """use tuple power and list comprehension, to sort dictionary items."""
        lst = sorted([(k,v) for k, v in counts.items()])

"""print out final desired result."""
print(lst)







