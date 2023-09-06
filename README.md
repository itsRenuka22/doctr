## To train english-hindi dual-lingual model:
- Clone this branch using git clone --branch English-Hindi https://github.com/iitb-research-code/doctr
- Add path to project folder containing doctr folder in PROJECT_FOLDER on line 5 of /references/recognition/train_pytorch.py
- Install dependencies using pip install -r requirements.txt
- Copy contents of ./data/Font/fonts_list.txt to pass to --font parameter while training
- For training from scratch: python references/recognition/train_pytorch.py crnn_vgg16_bn_hinglish --vocab hinglish --words_txt_path ./data/english_hindi_Compliant_plus.txt --epochs <int: num epochs> --train-samples <int: num_training_samples> --val-samples <int: num_validation_samples> --name <str: model_name> --font <str: list of font file paths (comma separated, without space), can find in ./data/fonts_list.txt>
- For training from checkpoint: add --resume <str: checkpoint_path>
- Specify arguments in angular brackets (<>) as per need
## Quick points about pipeline:
- Vocab for english and hindi combined is defined as "hinglish"
- After training, model will be saved in ./references/recognition/ as per --name argument
- Model architecture is defined in configs as "crnn_vgg16_bn_hinglish"
- Python version used is Python 3.8.10
