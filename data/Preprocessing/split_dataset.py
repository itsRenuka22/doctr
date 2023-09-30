import random
import os
import sys
if __name__=="__main__":
    # filename = "data/Text/english_hindi_Compliant_plus.txt"
    if(len(sys.argv)<2):
        print("Usage: python ./data/Preprocessing/split_dataset.py path/to/file_to_split")
        sys.exit(1)
    filename = sys.argv[1]
    if(os.path.isfile(filename)):
        with open(filename) as f:
            words = f.read().split("\n")
        val_output = open("data/Text/val.txt", "w")
        train_output = open("data/Text/train.txt", "w")
        test_output = open("data/Text/test.txt", "w")
        for word in words:
            thresh = random.random()
            if(thresh<=0.7):
                train_output.write(word+"\n")
            elif(thresh>0.7 and thresh<=0.9):
                val_output.write(word+"\n")
            else:
                test_output.write(word+"\n")
        print("Split dataset into train, test, validation")
        val_output.close()
        train_output.close()
        test_output.close()
    else:
        print(f"File {sys.argv[1]} not found")