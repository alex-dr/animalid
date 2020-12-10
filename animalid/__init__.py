"""Utility for importing text files as Python lists.

This module makes it possible to treat text files of words as module
attributes.

Every file in the lists/ directory will be read and converted to a list of
strings, which will become a module attribute with the same name as the name
of the file, minus the .txt extension.

This makes adding and maintaining these lists of words very easy while also
making them very accessible inside python.

To import these lists, simply import them like any other module attribute.

For example:

    from animalid import animals
    print(len(animals))
    print(animals[0])

"""
import glob
import os
import sys


MODULE = sys.modules[__name__]
DIRECTORY = os.path.dirname(os.path.realpath(__file__))


def read_file_to_list(filename):
    """Given a file in this directory, return a set containing every line."""
    with open(os.path.join(DIRECTORY, filename), "r") as f:
        return [word.strip() for word in f.readlines()]


for word_file in glob.glob(os.path.join(DIRECTORY, "lists/*.txt")):
    word_list = read_file_to_list(word_file)
    word_key = os.path.basename(word_file).rstrip(".txt")
    setattr(MODULE, word_key, word_list)
