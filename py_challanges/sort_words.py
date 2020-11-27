""" Python function to sort words in a string. """

""" First option
def sort_words(input):
    words = input.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return " ".join(words)
"""

def sort_words(input):

    def func(temp):
        return temp.lower()
        
    words = input.split()
    words.sort(key=func)
    return " ".join(words)
