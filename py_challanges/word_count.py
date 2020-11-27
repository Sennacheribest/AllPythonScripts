""" Python function to count number of unique words and how often each occurs. """
import re
from collections import Counter

def count_words(path):
    with open(path, encoding="utf-8") as file:
        words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        words = [word.upper() for word in words]
        print("\nTotal Words: ", len(words))

        word_counts = Counter()
        for word in words:
            word_counts[word] += 1

        print("\nTop 20 Used Words: ")
        for word in word_counts.most_common(20):
            print(word[0], "\t", word[1])
