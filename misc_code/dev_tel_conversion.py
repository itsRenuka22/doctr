import os
import pandas as pd
import shutil
from tqdm import tqdm

input_dir = '/data/BADRI/DATASETS/BENCHMARK/RECOGNITON/iiit_indic_words/telugu'
output_dir = '/data/BADRI/RECOGNITION/datasets/telugu/'


train_df = pd.read_csv(os.path.join(input_dir, 'train.txt'), sep=' ', names=['image', 'label'])
test_df = pd.read_csv(os.path.join(input_dir, 'test.txt'), sep=' ', names=['image', 'label'])
val_df = pd.read_csv(os.path.join(input_dir, 'val.txt'), sep=' ', names=['image', 'label'])


sets = ['train', 'test', 'val']

for set_ in sets:
    os.makedirs(os.path.join(output_dir, set_), exist_ok=True)    
    
    # try:
    df = pd.read_csv(os.path.join(input_dir, set_ + '.txt'), sep=' ', names=['image', 'label'])

    values = []
    count = 1
    for _, row in tqdm(df.iterrows()):
        row['image'] = os.path.join(input_dir, row['image'])
        
        # Copy from one location to another
        shutil.copy(row['image'], os.path.join(output_dir, set_, str(count) + '.jpg'))
        values.append([str(count) + '.jpg', row['label']])
        count += 1
        
    # save the dataframe
    pd.DataFrame(values, columns=['image', 'label']).to_csv(os.path.join(output_dir, set_ + '.txt'), index=False, header=False, sep=' ')