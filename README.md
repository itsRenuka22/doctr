## To train english-hindi dual-lingual model:
- Clone this branch using git clone --branch English-Hindi https://github.com/iitb-research-code/doctr
- Add path to project folder containing doctr folder in PROJECT_FOLDER on line 5 of /references/recognition/train_pytorch.py
- Install dependencies using pip install -r requirements.txt
- Copy contents of ./data/Fonts/fonts_list.txt to pass to --font parameter while training
- For training from scratch: python references/recognition/train_pytorch.py crnn_vgg16_bn_hinglish --vocab hinglish --words_txt_path ./data/english_hindi_Compliant_plus.txt --epochs <int: num epochs> --train-samples <int: num_training_samples> --val-samples <int: num_validation_samples> --name <str: model_name> --font <str: list of font file paths (comma separated, without space), can find in ./data/fonts_list.txt>
- For training from checkpoint: add --resume <str: checkpoint_path>
- Specify arguments in angular brackets (<>) as per need
- Python 3.8.10 is used
## Quick points about pipeline:
- Vocab for english and hindi combined is defined as "hinglish"
- After training, model will be saved in ./references/recognition/ as per --name argument
- Model architecture is defined in configs as "crnn_vgg16_bn_hinglish"
## Changes made by me:
- Created and added hinglish vocabulary to vocabs.py
- Created crnn_vgg16_bn_hinglish model in ./doctr/models/recognition/crnn/pytorch.py by adding configuration and wrapper function and adding model to ./doctr/models/recognition/zoo.py
- Altered ./references/recognition/train_pytorch.py to invoke custom word generator for synthetic data generation for training
- Explored multiple large English and Hindi corpora and compiled data to form extensively large list of words, then processed words to remove duplicates and ensure compliance to vocabulary in ./data
- Explored and downloaded fonts that work for both Devanagari and English simultaneously and compiled list in ./data/Fonts
