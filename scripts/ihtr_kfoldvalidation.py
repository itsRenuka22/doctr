import pandas as pd
import os
import json
import argparse
import shutil
from sklearn.model_selection import KFold


def merge_data(data_dir):    
    
    src_dir = data_dir + 'total/'
    val = len(os.listdir(src_dir))
    for file in os.listdir(data_dir + 'test/'):
        file_val = int(file.split('.')[0])
        shutil.copy2(data_dir + 'test/' + file, data_dir + 'total/' + str(val) + '.jpg')
        val += 1
     
    for file in os.listdir(data_dir + 'val/'):
        file_val = int(file.split('.')[0])
        shutil.copy2(data_dir + 'val/' + file, data_dir + 'total/' + str(val) + '.jpg')
        val += 1
        
    



def create_json_files(data_dir):
    vocab_df = pd.read_csv(os.path.join(data_dir, 'vocab.txt'), sep=" ", names=["label"])
    vocab_df['index'] = vocab_df.index

    train_df = pd.read_csv(data_dir + 'train.txt', sep=" ", names=["image_path", "index"])
    val_df = pd.read_csv(data_dir + 'val.txt', sep=" ", names=["image_path", "index"])
    test_df = pd.read_csv(data_dir + 'test.txt', sep=" ", names=["image_path", "index"])

    train_len = train_df.shape[0]

    train_df['image_path'] = train_df['image_path'].apply(lambda x: x.split('/')[-1][:-1])

    test_df['image_path'] = test_df['image_path'].apply(lambda x: x.split('/')[-1][:-1].split('.')[0])
    test_df['image_path'] = test_df['image_path'].apply(lambda x: str(train_len + int(x)) + '.jpg')
    train_df = pd.concat([train_df, test_df], ignore_index=True)

    val_df['image_path'] = val_df['image_path'].apply(lambda x: x.split('/')[-1][:-1].split('.')[0])
    val_df['image_path'] = val_df['image_path'].apply(lambda x: str(train_len + int(x)) + '.jpg')
    train_df = pd.concat([train_df, val_df], ignore_index=True)

    result_df = pd.merge(train_df, vocab_df, on='index', how='left')


    kf = KFold(n_splits = 5, shuffle = False)
    result = list(kf.split(result_df))

    count=0
    
    if not os.path.exists(data_dir + 'kfold/'):
        os.makedirs(data_dir + 'kfold/')

    for value in result:
        train = result_df.iloc[value[0]]
        val =  result_df.iloc[value[1]]
        
        train_data = dict(zip(train.image_path, train.label))
        val_data = dict(zip(val.image_path, val.label))
        
        with open(data_dir + 'kfold/train' + str(count)+'.json', 'w', encoding='utf-8') as f:
            json.dump(train_data, f, ensure_ascii=False, indent=4)
            
        with open(data_dir + 'kfold/val' + str(count)+'.json', 'w', encoding='utf-8') as f:
            json.dump(val_data, f, ensure_ascii=False, indent=4)
            
        count +=1
  
  
def parse_args():
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--data_dir", type=str, default=None, help="path to the input folder")
    
    args = parser.parse_args()
    return args
            
if __name__ == "__main__":
    args = parse_args()
    create_json_files(args.data_dir)
    merge_data(args.data_dir)





