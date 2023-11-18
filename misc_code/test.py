import os
from tqdm import tqdm
import torch
import argparse
import sys
import pandas as pd
sys.path.append(".")
from doctr.io import DocumentFile
from doctr.models import parseq, crnn_vgg16_bn, master, vitstr_small
from doctr.models.recognition.predictor import RecognitionPredictor
from doctr.models.preprocessor import PreProcessor

# If only CPU is there use cpu instead of cuda
os.environ["USE_TORCH"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


def load_model(model, saved_model, vocab_file):
    
    if(isinstance(vocab_file, str)):
        with open(vocab_file) as f:
            vocab = f.read()
    else:
        print("Please enter valid vocab file path (--vocab_file path/to/file)")
        return
    
    if(model=='parseq'):
        reco_model = parseq(pretrained=False, vocab=vocab)
    elif(model=='master'):
        reco_model = master(pretrained=False, vocab=vocab)
    elif(model=='vitstr_small'):
        reco_model = vitstr_small(pretrained=False, vocab=vocab)
    else:
        reco_model = crnn_vgg16_bn(pretrained=False, vocab=vocab)
    reco_param = torch.load(saved_model, map_location="cuda")
    reco_model.load_state_dict(reco_param)
    reco_predictor = RecognitionPredictor(PreProcessor((32, 128), preserve_aspect_ratio=True, batch_size=1, mean=(0.694, 0.695, 0.693), std=(0.299, 0.296, 0.301)), reco_model)  
    return reco_predictor

def get_result(input_file, model_predictor):
    doc = DocumentFile.from_images(input_file)    
    result = model_predictor(doc)[0][0]  
    return result
    

def parse_args():
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input_file", type=str, default=None, help="path to the input folder")
    parser.add_argument("-m", "--model", type=str, default='crnn_vgg16_bn', help="Model name")
    parser.add_argument("-r", "--rec_model", type=str, default=None, help="Path to saved recognition model weights")
    parser.add_argument("-v", "--vocab_file", type=str, default=None, help="Path to vocab file generated during training")
    parser.add_argument("-o", "--output", type=str, default=None, help="Output file name")
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    
    model = load_model(args.model, args.rec_model, args.vocab_file)
    
    results = {}
    files = sorted(os.listdir(args.input_file))
    for file in tqdm(files):
        results[file] = get_result(args.input_file + file, model)
        
    # save as txt file through pandas dataframe
    
    df = pd.DataFrame(results.items(), columns=['filename', 'text'])
    df.to_csv(args.output + '.txt', index=False, header=False, sep=' ')