import os

os.chdir('./doctr/')


languages  = ['bengali', 'gujarati', 'gurumukhi', 'hindi', 'kannada', 'malayalam', 'tamil', 'telugu', 'odia', 'urdu']
languages = ['tamil', 'kannada', 'odia']
models = ['parseq', 'crnn_vgg16_bn', 'master', 'vitstr_small', 'crnn_mobilenet_v3_small', 'vitstr_base', 'sar_resnet31']
models = ['parseq']


DEVICE = 0


for model in models:
    for lang in languages:
        trained_model = './../models/' + model + '_' + lang + '.pt'
        print(trained_model)
        if(os.path.exists(trained_model)):
            if(lang == 'hindi') or lang=='telugu':
                command = 'python references/recognition/evaluate_pytorch_ihtr.py ' + model + ' --train_path /data/BADRI/RECOGNITION/datasets/' + lang + '/ -b 1 --device ' + str(DEVICE) + ' --resume ' + trained_model + ' --test-only --vocab iiit_' + lang + ' --out_file ' + model + '_' + lang
            else:
                command = 'python references/recognition/evaluate_pytorch_ihtr.py ' + model + ' --train_path /data/BADRI/DATASETS/BENCHMARK/RECOGNITON/iiit_indic_words/' + lang + '/ -b 1 --device ' + str(DEVICE) + ' --resume ' + trained_model + ' --test-only --vocab iiit_' + lang + ' --out_file ' + model + '_' + lang
            # command = 'python get_predictions.py -i ./../../data/' + lang + '/test/ -r ' + trained_model + ' -m ' + model + ' -v iiit_' + lang + ' -o ./../results/' + model + '_' + lang
            os.system(command)



