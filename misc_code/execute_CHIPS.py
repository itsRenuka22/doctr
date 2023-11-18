import os
import time

os.chdir('./doctr/')

languages  = ['bengali', 'gujarati', 'gurumukhi', 'hindi', 'kannada', 'malayalam', 'tamil', 'telugu', 'odia', 'urdu']
# languages = ['kannada', 'malayalam', 'tamil']
# languages = ['urdu']
models = ['master', 'vitstr_small', 'crnn_mobilenet_v3_small', 'crnn_vgg16_bn', 'sar_resnet31', 'parseq']
models = ['parseq']

# models = ['crnn_mobilenet_v3_small']


DEVICE = 0

out_files = []
# out_file = 'gt_chips_1'

out_files = ['finetuned_CHIPS1', 'gt_CHIPS1', 'pretrained_CHIPS1']
data = {}

out_files = ['pretrained_CHIPS1']

for out_file in out_files:
    for model in models:
        times = []
        for lang in languages:
            
            start_time = time.time()

            trained_model = './../models/' + model + '_' + lang + '.pt'
            command = f'python references/recognition/evaluate_pytorch_CHIPS.py {model} --train_path ./../../../OCR/results/intermediate/{out_file}/{lang}/ --out_file {out_file} -b 1 --device {DEVICE} --resume {trained_model} --vocab iiit_{lang} --test-only'
            os.system(command)
            
            end_time = time.time()
            print("Time taken for ", model, lang, " is ", end_time - start_time)
            times.append(end_time - start_time)
        data[out_file + '_' + model] = times
        # exit()
    
# save json
import json
with open('all_results_final_parseq_pretrained.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
        







