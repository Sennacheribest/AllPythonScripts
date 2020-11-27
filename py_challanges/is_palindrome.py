""" Python function to determine if a given string is a palindrome. """

""" Import reqular expression. """
import re

""" Build the logic inside function. """
def is_palindrome(phrase):
    forwards = "".join(re.findall(r"[a-z]", phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards
