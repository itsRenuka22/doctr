import os
import json
import cv2
import re
import pandas as pd
from tqdm import tqdm

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]


languages = ['bengali', 'gujarati', 'gurumukhi', 'hindi', 'kannada', 'malayalam', 'odia', 'tamil', 'telugu', 'urdu']



DATA_DIR = '/data/BADRI/OCR/data/CHIPS_synth/'
sets = ['test', 'val', 'train']

sets = ['']
    
for typeset in sets:
    
    input_dir = os.path.join(DATA_DIR, typeset)
    
    final_data = {}
    count = 0
    for file in tqdm(sorted(os.listdir(input_dir +'/txt/'))):
        
        df = pd.read_csv(os.path.join(input_dir, 'txt', file), sep=' ', header=None, names=['label', 'x1', 'y1', 'x2', 'y2'])
        img = cv2.imread(os.path.join(input_dir, 'images', file[:-4] + '.jpg'))
        
        image_data = {}
        height, width, _ = img.shape
        image_data['img_dimensions'] = (height, width)
        image_data['img_hash'] = file[:-4] + '.jpg'
        
        bbox_data = []
        for _, row in df.iterrows():
            x1, y1, x2, y2 = int(row['x1']), int(row['y1']), int(row['x2']), int(row['y2'])
            bbox_data.append([[x1, y1],[x2, y1],[x2, y2],[x1, y2]])
            
        image_data['polygons'] = bbox_data
        final_data[file[:-4] + '.jpg'] = image_data
        
        if(height !=1024):
            
            with open(os.path.join(DATA_DIR, typeset, languages[count] + '.json'), "w") as json_file:
                json.dump(final_data, json_file, indent=4)
            final_data = {}
            count += 1
            
            
            
        #Save data in json format
        with open(os.path.join(DATA_DIR, typeset, 'labels.json'), "w") as json_file:
            json.dump(final_data, json_file, indent=4)
        