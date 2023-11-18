import os

os.chdir('./doctr/')

# LANGUAGE = 'odia'
# MODEL = 'master'
# EPOCHS = 500
# BATCH_SIZE = 128
# LEARNING_RATE = 0.001
# DEVICE = 1
# TRAIN_PATH = '/data/BADRI/DATASETS/BENCHMARK/RECOGNITON/iiit_indic_words/'



# BACKGROUND = False

# languages = ['tamil', 'telugu', 'malayalam', 'kannada']
# languages = ['gujarati', 'gurumukhi']

languages = ['malayalam', 'kannada']
RESUME = True
languages = [ 'tamil', 'telugu', 'odia', 'urdu']
languages = ['labels']
EVALUATION = False


for lang in languages:

    if(EVALUATION):
        command = f'python references/detection/train_pytorch_CHIPS.py /data/BADRI/OCR/data/CHIPS1/train/ /data/BADRI/OCR/data/CHIPS1/test/ db_resnet50 --name {lang} --epochs 5 --b 1 --device 0 --resume ./../models/detection/finetuned.pt --test-only'  
    else:
        command = f'python references/detection/train_pytorch_CHIPS.py /data/BADRI/OCR/data/CHIPS1/train/ /data/BADRI/OCR/data/CHIPS1/val/ db_resnet50 --name {lang} --epochs 5 --b 8 --device 0'
        
        if(RESUME):
            command += f' --resume ./../models/detection/finetuned.pt'
    
    print(command)
    # os.system(command)