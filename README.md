## To train generic model for any given source txt file containing line separated-words:
- Clone this branch using git clone --branch Generic https://github.com/iitb-research-code/doctr
- Add path to project folder containing doctr folder in PROJECT_FOLDER on line 5 of /references/recognition/train_pytorch.py
- Install dependencies using ```pip install -r requirements.txt```
- Run the following to split dataset: ```python ./data/split_dataset.py <str: path to txt file>```
- For training from scratch: 
```
python references/recognition/train_pytorch.py crnn_vgg16_bn_generic --words_txt_path <str: path to txt source file> --train_txt_path <str: path to train txt file generated using split_dataset.py> --val_txt_path <str: path to val txt file generated using split_dataset.py> --epochs <int: num epochs> --train-samples <int: num_training_samples> --val-samples <int: num_validation_samples> --name <str: model_name> --font <str: list of font file paths (comma separated, without space)>
```
- For training from checkpoint: add --resume <str: checkpoint_path>
- Specify arguments in angular brackets (<>) as per need
- Python 3.8.10 is used
## Quick points about pipeline:
- Branched from English-Hindi
- Vocab is generated automatically by ./data/vocab_generation.py from txt file
- If --vocab parameter is passed as generic, or not invoked at all, the automatic vocab generation will be called
- After training, model will be saved in ./references/recognition/ as per --name argument
- After training, generated vocab will be saved in ./data/Vocabs as per model name.
- Model architecture is defined in configs as "crnn_vgg16_bn_generic"

## Instructions for inference:
- Run command python scripts/inference_recognition.py --input_file <str: path to input image> --rec_model <str: path to saved recognition model weights to use for inference> --vocab_file <str: path to generated vocab file for trained model (saved in data / Vocabs) > --output <str: output_filename.json>
## Changes made by me:
- Created crnn_vgg16_bn_generic model in ./doctr/models/recognition/crnn/pytorch.py by adding configuration and wrapper function and adding model to ./doctr/models/recognition/zoo.py
- Altered ./references/recognition/train_pytorch.py to invoke automated vocab generation if --vocab is set to generic or not provided
- Adapted inference code to work with generic model.
