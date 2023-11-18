# Calculate CRR and WRR given txt file of results and ground truth in two different dataframes which are loaded through csv files using jiwer library
import argparse
import fastwer
import pandas as pd

def calculate_crr_wrr(results, ground_truth):
    crr = 0
    wrr = 0
    cer = fastwer.score(results.tolist(), ground_truth.tolist(), char_level=True)
    wer = fastwer.score(results.tolist(), ground_truth.tolist())
    return 100- cer, 100-wer
    # for i in range(len(results)):
    #     crr += fastwer.score([results[i]], [ground_truth[i]], char_level=True)
    #     wrr += fastwer.score([results[i]], [ground_truth[i]])
    # crr /= len(results)
    # wrr /= len(results)
    # return crr, wrr

def parse_args():
    parser = argparse.ArgumentParser(description="Documents OCR Input Arguments", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--predictions_file", type=str, default=None, help="path to the predictions file")
    parser.add_argument("-g", "--ground_truth_file", type=str, default=None, help="path to the GT file")

    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    # predictions = pd.read_csv(args.predictions_file)  
    # predictions = pd.read_csv(args.predictions_file, names=['filename', 'text'])  
    predictions = pd.read_csv(args.predictions_file, names=['filename', 'text'], sep=' ')  
    ground_truth = pd.read_csv(args.ground_truth_file, names=['filename', 'text'], sep=' ')
    
    df = pd.merge(predictions, ground_truth, on='filename')
    # df = pd.read_csv(args.ground_truth_file, names=['filename', 'text_x', 'text_y'], sep=' ')
    
    crr, wrr = calculate_crr_wrr(df['text_x'], df['text_y'])
    
    
    
    print("CRR: ", crr)
    print("WRR: ", wrr)