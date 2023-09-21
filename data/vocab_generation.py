import sys
import os

def get_unique_chars_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    unique_chars = set()
    for line in lines:
        unique_chars.update(set(line))
    return unique_chars

def GetVocab(filename):
    if not os.path.exists(filename):
        print("File {} does not exist".format(filename))
        sys.exit(1)
    unique_chars = "".join(sorted(list(get_unique_chars_from_file(filename))))   
    # print("Unique characters in file {} are :\n {}".format(filename, unique_chars))
    return unique_chars

# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         print("Usage: python vocab_generation.py <filename>")
#         sys.exit(1)
#     filename = sys.argv[1]
#     if not os.path.exists(filename):
#         print("File {} does not exist".format(filename))
#         sys.exit(1)
#     unique_chars = sorted(list(get_unique_chars_from_file(filename)))    
#     print("Unique characters in file {} are :\n {}".format(filename, unique_chars))