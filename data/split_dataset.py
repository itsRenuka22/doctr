import random
import os
import sys
if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_dataset.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    if(os.path.isfile(filename)):
        with open(filename) as f:
            words = f.read().split("\n")
        val_output = open("data/val.txt", "w")
        train_output = open("data/train.txt", "w")
        test_output = open("data/test.txt", "w")
        for word in words:
            thresh = random.random()
            if(thresh<=0.7):
                print(f"Writing {word} to train_output")
                train_output.write(word+"\n")
            elif(thresh>0.7 and thresh<=0.9):
                print(f"Writing {word} to val_output")
                val_output.write(word+"\n")
            else:
                print(f"Writing {word} to test_output")
                test_output.write(word+"\n")
        val_output.close()
        train_output.close()
        test_output.close()
    else:
        print("File not found")