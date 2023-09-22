import os
import json
import torch
import argparse
import sys
sys.path.append("./..")
from doctr.io import DocumentFile
from doctr.models import crnn_vgg16_bn_generic
from doctr.models.recognition.predictor import RecognitionPredictor
from doctr.models.preprocessor import PreProcessor

# If only CPU is there use cpu instead of cuda
os.environ["USE_TORCH"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"



def get_result(args):
    doc = DocumentFile.from_images(args.input_file)
    if(isinstance(args.vocab_file, str)):
        with open(args.vocab_file) as f:
            vocab = f.read()
    else:
        print("Please enter valid vocab file path (--vocab_file path/to/file)")


    #Recognition model
    reco_model = crnn_vgg16_bn_generic(pretrained=False, vocab=vocab)
    reco_param = torch.load(args.rec_model, map_location="cuda")
    reco_model.load_state_dict(reco_param)
    reco_predictor = RecognitionPredictor(PreProcessor((32, 128), preserve_aspect_ratio=True, batch_size=1, mean=(0.694, 0.695, 0.693), std=(0.299, 0.296, 0.301)), reco_model)        



    result = reco_predictor(doc)[0][0]
    
    
    
def parse_args():
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input_file", type=str, default=None, help="path to the input folder")
    parser.add_argument("-d", "--det_model", type=str, default=None, help="Detection model directory")
    parser.add_argument("-r", "--rec_model", type=str, default=None, help="Path to saved recognition model weights")
    parser.add_argument("-v", "--vocab_file", type=str, default=None, help="Path to vocab file generated during training")
    parser.add_argument("-o", "--output", type=str, default=None, help="Output file name")
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    get_result(args)