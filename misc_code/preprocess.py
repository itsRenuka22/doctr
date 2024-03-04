import argparse

from sklearn.model_selection import train_test_split
import os
import random

from doctr.datasets import VOCABS

class PreprocessWordDataset:
    def __init__(self, input_file, valid_vocab):
        self.input_file = input_file
        self.valid_vocab = valid_vocab

    def load_file_as_words(self):

        with open(self.input_file, encoding="utf-8") as f:
            data = f.read()
        
        words = list(map(lambda x: x.strip(),data.split()))
        return words
    
    def filter_words(self, words):

        filtered_words = []

        for word in words:
            include = True
            for i in word:
                if i not in self.valid_vocab:
                    include = False
            if include:
                filtered_words.append(word)
        
        return filtered_words
    
    def split_data(self, words):
        return train_test_split(words, test_size = 0.1, random_state= 24)

    def __call__(self, out_dir, sample = None, unique = False, continue_check = False):
        words = self.load_file_as_words()
        print(f"There are totally {len(words)} words in the file.")
        filtered = self.filter_words(words)
        print(f"There are totally {len(filtered)} valid words in the file.")

        if unique:
            filtered = list(set(filtered))
            print(f"There are totally {len(filtered)} unique valid words in the file.")
        if sample:
            filtered = random.sample(filtered, int(len(filtered) * sample))
            print(f"Sampled only {len(filtered)} random words from data.")

        if continue_check:
            c = input("Do you want to save?(y/n)")
            if c!="y":
                return
        train, val = self.split_data(filtered)

        train = "\n".join(train)
        val = "\n".join(val)

        if not os.path.exists(out_dir):
            os.mkdir(out_dir)        

        try:
            with open(os.path.join(out_dir,"train.txt"),"w",encoding="utf-8") as f:
                f.write(train)
            with open(os.path.join(out_dir,"val.txt"),"w",encoding="utf-8") as f:
                f.write(val)

            print(f"The processed words for given vocabulary is stored in {out_dir} as train.txt and val.txt")
        except:
            raise "Unable to Create File. Failed"

def main(args):
    valid_vocab = VOCABS['tamil']
    preprocess = PreprocessWordDataset(args.input_path,valid_vocab)
    preprocess(args.output_path, sample = args.sample, unique=args.unique, continue_check=args.continue_check)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess Data")
    parser.add_argument("--input_path", type=str, help="Path to input data")
    parser.add_argument("--output_path", type=str, help="Path to output directory")
    parser.add_argument("--vocab", type=str, help="vocab key in VOCAB dictionary")
    parser.add_argument("--sample", type=float, help="Sample value")
    parser.add_argument("--unique", action="store_true", help="Filter only unique words")
    parser.add_argument("--continue_check", action="store_true", help="If set then ask before saving the data.")
    args = parser.parse_args()
    
    main(args)