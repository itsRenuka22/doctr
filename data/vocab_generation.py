import sys
import os

def get_unique_chars_from_file(filename):
    """Reads input file line by line and generates a set of unique characters from file

    Args:
        filename (str): Input words txt file path to generate vocab from

    Returns:
        set: A set of unique characters
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    unique_chars = set()
    for line in lines:
        unique_chars.update(set(line))
    return unique_chars

def GetVocab(filename):
    """Generates the vocabulary from given filename by calling get_unique_chars_from_file.

    Args:
        filename (str): Input words txt file path to generate vocab from

    Returns:
        str: generated vocab as a string
    """
    if not os.path.exists(filename):
        print("File {} does not exist".format(filename))
        sys.exit(1)
    unique_chars = "".join(sorted(list(get_unique_chars_from_file(filename))))    
    print("Unique characters in file {} are :\n {}".format(filename, unique_chars))
    return unique_chars
