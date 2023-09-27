"""This script is used to combine different txt sources of words into a single file
    For usage: python ./data/merge_txt.py filename1 filename2...filenameN output_filename"""
import sys
import os
import argparse

def parse_args():
    """Argument parser

    Returns:
        argparse.Namespace 
    """
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--input_filenames", type=str, default=None, help="comma separated filenames")
    parser.add_argument("--output_file", type=str, default=None, help="Output file to create")
    args = parser.parse_args()
    return args
if __name__=="__main__":
    args=parse_args()
    input_files = args.input_filenames.split(",")
    words=[]
    #Read all input files and append to list of words
    for file in input_files:
        with open(file) as f:
            words+=(f.read().split("\n"))
    #Remove duplicates
    words = list(set(words))
    #Write output to output file
    output = "\n".join(words)
    if(isinstance(args.output_file, str)):
        try:
            with open(args.output_file, "w") as f:
                print(f"Writing {len(words)} total unique words to {args.output_file}")
                f.write(output)
        except FileNotFoundError:
            print(f"Unable to find {args.output_file}")
    else:
        print("Please provide --output_file argument")
        sys.exit(1)