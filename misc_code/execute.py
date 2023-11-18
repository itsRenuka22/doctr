import os

os.chdir('./doctr/')

LANGUAGE = 'odia'
MODEL = 'master'
EPOCHS = 500
BATCH_SIZE = 128
LEARNING_RATE = 0.001
DEVICE = 1
TRAIN_PATH = '/data/BADRI/DATASETS/BENCHMARK/RECOGNITON/iiit_indic_words/'

RESUME = False

BACKGROUND = False

if(BACKGROUND):
    if not (RESUME):
        command = 'nohup python references/recognition/train_pytorch_ihtr.py ' + MODEL + ' --train_path ' + TRAIN_PATH + LANGUAGE + '/ --vocab iiit_' + LANGUAGE + ' --name ' + MODEL + '_' + LANGUAGE + ' --epochs ' + str(EPOCHS) + ' --b ' + str(BATCH_SIZE) + ' --device '+ str(DEVICE) + ' --lr ' + str(LEARNING_RATE) + ' > ' + MODEL + '_' + LANGUAGE + '.out &'
    else:
        print("Resuming old state")
        command = 'nohup python references/recognition/train_pytorch_ihtr.py ' + MODEL + ' --train_path ' + TRAIN_PATH + LANGUAGE + '/ --vocab iiit_' + LANGUAGE + ' --name ' + MODEL + '_' + LANGUAGE + ' --epochs ' + str(EPOCHS) + ' --b ' + str(BATCH_SIZE) + ' --device '+ str(DEVICE) + ' --lr ' + str(LEARNING_RATE) + ' --resume ./../models/' + MODEL + '_' + LANGUAGE  + '.pt > ' + MODEL + '_' + LANGUAGE + '.out &'
else:
    if not (RESUME):
        command = 'python references/recognition/train_pytorch_ihtr.py ' + MODEL + ' --train_path ' + TRAIN_PATH + LANGUAGE + '/ --vocab iiit_' + LANGUAGE + ' --name ' + MODEL + '_' + LANGUAGE + ' --epochs ' + str(EPOCHS) + ' --b ' + str(BATCH_SIZE) + ' --device '+ str(DEVICE) + ' --lr ' + str(LEARNING_RATE)
    else:
        print("Resuming old state")
        command = 'python references/recognition/train_pytorch_ihtr.py ' + MODEL + ' --train_path ' + TRAIN_PATH + LANGUAGE + '/ --vocab iiit_' + LANGUAGE + ' --name ' + MODEL + '_' + LANGUAGE + ' --epochs ' + str(EPOCHS) + ' --b ' + str(BATCH_SIZE) + ' --device '+ str(DEVICE) + ' --lr ' + str(LEARNING_RATE) + ' --resume ./../models/' + MODEL + '_' + LANGUAGE  + '.pt'

print(command)
# os.system(command)