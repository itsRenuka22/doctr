import os
import json
import shutil
import argparse
import pandas as pd
from tqdm import tqdm

def get_vocab(file_path):
    
    unique_characters = set()
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            unique_characters.update(line)  
    
    result = sorted(list(unique_characters))
    print("\nNo of unique characters in data:",len(result))

    unique_chars =  "".join(result)
    print("\nUnique characters:", unique_chars)
    print("Use the above vocab to update in the vocabs.py file accordingly")


def create_json_files(data_dir, dev_tel=False, output_dir=None):
    
    typesets = ['train','val','test']
        
    for sets in typesets:
        
        file_loc = os.path.join(data_dir, sets)
        data_df = pd.read_csv(file_loc + '.txt', sep=" ", names=["image_path", "label"])
            
        if(dev_tel):
            os.makedirs(os.path.join(output_dir, sets), exist_ok=True)  
            
            values, count = [], 1
            for _, row in tqdm(data_df.iterrows()):
                file_value = os.path.join(data_dir, row['image_path'])

                shutil.copy(file_value, os.path.join(output_dir, sets, str(count) + '.jpg'))
                values.append([str(count) + '.jpg', row['label']])
                count += 1
            
            result_df = pd.DataFrame(values, columns=['image_path', 'label'])
            result_df.to_csv(os.path.join(output_dir, sets + '.txt'), index=False, header=False, sep=' ')
            file_loc = os.path.join(output_dir, sets)
        else:   
            vocab_df = pd.read_csv(os.path.join(data_dir, 'vocab.txt'), sep=" ", names=["label"])
            vocab_df['index'] = vocab_df.index
            
            data_df.columns = ['image_path', 'index']
            data_df['image_path'] = data_df['image_path'].apply(lambda x: x.split('/')[-1][:-1])
            result_df = pd.merge(data_df, vocab_df, on='index', how='left')

        data = dict(zip(result_df.image_path, result_df.label))
        with open(file_loc + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    print("Json file creation: Done")

    
def parse_args():
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--data_dir", type=str, default=None, help="path to the input folder")
    parser.add_argument("-d", "--dev_tel", action="store_true", help="Use this flag if the dataset is devanagari_telugu and is processed for first time")
    parser.add_argument("-o", "--out_dir",  type=str, default=None, help="path to the output folder, used only for devanagari_telugu")

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    create_json_files(args.data_dir, dev_tel=args.dev_tel, output_dir=args.out_dir)
    
    if(args.dev_tel):
        get_vocab(os.path.join(args.data_dir + 'lexicon.txt'))
    else:
        get_vocab(os.path.join(args.data_dir + 'vocab.txt'))