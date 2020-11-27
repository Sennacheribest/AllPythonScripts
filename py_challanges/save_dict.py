""" Python function to save a dictionary to file. """

import pickle

def save_dict(name, path):
    with open(path, "wb") as file:
        pickle.dump(name, file)

def load_dict(path):
    with open(path, "rb") as file:
        return pickle.load(file)
