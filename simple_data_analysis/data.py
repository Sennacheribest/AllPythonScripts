"""Python code to extract clean data form huge, mail-box log file, then apply some data analysis."""

"""Import regular experission module."""
import re

"""Ask user for a file."""
fname = input("Enter a file: ")

"""This line is for lazy SysAdmins like me."""
if len(fname) < 1: fname = "mbox-short.txt"

"""Open given file with try-except method."""  
fhand = open(fname)

"""Prepare an empty list to gather the required data."""
numlist = list()

"""Read through the file line by line."""
for line in fhand:
    """Get rid of (\n) at each end of line."""
    line = line.rstrip()
    """Apply regular experssion pattern to extrac the required data from each line."""
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    """Do sanity check to ignore any retured empty value."""
    if len(stuff) < 1: continue
    """Convert the returend string values into float one."""
    num = float(stuff[0])
    """Data analysis and methods."""
    numlist.append(num)
    minval = min(numlist)
    maxval = max(numlist)

"""Print out final results."""
print("\nMinimum number found:\t {}".format(minval))
print("Maximum number found:\t {}".format(maxval))
print("\n The range value:\t {}".format(maxval - minval))
print("Median of values:\t {:.4f}".format(sum(numlist) / len(numlist)))  
