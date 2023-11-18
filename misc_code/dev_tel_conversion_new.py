import os
import pandas as pd
import shutil
from tqdm import tqdm

input_dir = '/data/BADRI/DATASETS/BENCHMARK/RECOGNITON/HANDWRITTEN/IIIT_INDIC_HW_WORDS/telugu/'
output_dir = '/data/BADRI/DATASETS/BENCHMARK/RECOGNITON/HANDWRITTEN/IIIT_INDIC_HW_WORDS/telugu_pro/'


# train_df = pd.read_csv(os.path.join(input_dir, 'train.txt'), sep=' ', names=['image', 'label'])
# test_df = pd.read_csv(os.path.join(input_dir, 'test.txt'), sep=' ', names=['image', 'label'])
# val_df = pd.read_csv(os.path.join(input_dir, 'val.txt'), sep=' ', names=['image', 'label'])


sets = ['train', 'test', 'val']

for set_ in sets:
    os.makedirs(os.path.join(output_dir, set_, 'images'), exist_ok=True)    
    
    # try:
    df = pd.read_csv(os.path.join(input_dir, set_, set_ + '_gt.txt'), sep='\t', names=['image', 'label'])

    values = []
    count = 1
    for _, row in tqdm(df.iterrows()):
        row['image'] = os.path.join(input_dir, set_, row['image'])
        
        # Copy from one location to another
        shutil.copy(row['image'], os.path.join(output_dir, set_, 'images', str(count) + '.jpg'))
        values.append(['images/' + str(count) + '.jpg', row['label']])
        count += 1
        
    # save the dataframe
    pd.DataFrame(values, columns=['image', 'label']).to_csv(os.path.join(output_dir, set_, set_ + '_gt.txt'), index=False, header=False, sep='\t')