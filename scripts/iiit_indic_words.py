import os
import json
import argparse
import pandas as pd

def get_unique_characters(file_path):
    unique_characters = set()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace and newline characters
            unique_characters.update(line)  # Add characters from the line to the set
    
    
    result = sorted(list(unique_characters))
    print("\nNo of unique characters in data:",len(result))

    return "".join(result)


def create_json_files(data_dir):
    vocab_df = pd.read_csv(os.path.join(data_dir, 'vocab.txt'), sep=" ", names=["label"])
    vocab_df['index'] = vocab_df.index

    typesets = ['train','val','test']
    for sets in typesets:
        
        file_loc = os.path.join(data_dir, sets)
        data_df = pd.read_csv(file_loc + '.txt', sep=" ", names=["image_path", "index"])
        
        data_df['image_path'] = data_df['image_path'].apply(lambda x: x.split('/')[-1][:-1])

        
        result_df = pd.merge(data_df, vocab_df, on='index', how='left')

        data = dict(zip(result_df.image_path, result_df.label))
        
        
        with open(file_loc + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    print("Json file creation: Done")

def get_vocab(data_dir):
    unique_chars = get_unique_characters(os.path.join(data_dir, 'vocab.txt'))
    print("Unique characters:", unique_chars)
    print("Use the above vocab to update in the vocabs.py file accordingly")


def parse_args():
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--data_dir", type=str, default=None, help="path to the input folder")
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    create_json_files(args.data_dir)
    get_vocab(args.data_dir)