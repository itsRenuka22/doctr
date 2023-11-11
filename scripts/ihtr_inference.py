import os
import json
import torch
import argparse

from doctr.io import DocumentFile
from doctr.models import crnn_vgg16_bn, db_resnet50
from doctr.models.predictor import OCRPredictor
from doctr.models.detection.predictor import DetectionPredictor
from doctr.models.recognition.predictor import RecognitionPredictor
from doctr.models.preprocessor import PreProcessor
from doctr.datasets.vocabs import VOCABS

# If only CPU is there use cpu instead of cuda
os.environ["USE_TORCH"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"



def get_result(args):
    doc = DocumentFile.from_images(args.input_file)

    # Detection model
    det_model = db_resnet50(pretrained=True)
    det_param = torch.load(args.det_model, map_location="cuda")
    det_model.load_state_dict(det_param)
    det_predictor = DetectionPredictor(PreProcessor((1024, 1024), batch_size=1, mean=(0.798, 0.785, 0.772), std=(0.264, 0.2749, 0.287)), det_model)

    #Recognition model
    reco_model = crnn_vgg16_bn(pretrained=False, vocab=VOCABS[args.vocab])
    reco_param = torch.load(args.rec_model, map_location="cuda")
    reco_model.load_state_dict(reco_param)
    reco_predictor = RecognitionPredictor(PreProcessor((32, 128), preserve_aspect_ratio=True, batch_size=1, mean=(0.694, 0.695, 0.693), std=(0.299, 0.296, 0.301)), reco_model)        



    predictor = OCRPredictor(det_predictor, reco_predictor)

    result = predictor(doc)
    json_output = result.export()
    result.show(doc)


    with open(args.output, 'w') as f:
        json.dump(json_output, f, indent=4)
    
    
def parse_args():
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input_file", type=str, default=None, help="path to the input folder")
    parser.add_argument("-d", "--det_model", type=str, default=None, help="Detection model directory")
    parser.add_argument("-r", "--rec_model", type=str, default=None, help="Recognition Model Directory")
    parser.add_argument("-v", "--vocab", type=str, default=None, help="Vocabulary of the language")
    parser.add_argument("-o", "--output", type=str, default=None, help="Output file name")
    
    args = parser.parse_args()
    return args
            
if __name__ == "__main__":
    args = parse_args()
    get_result(args)


