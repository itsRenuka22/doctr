# Synthesis DocTR


## Installation

```
1. git clone https://github.com/iitb-research-code/doctr.git
2. cd doctr
3. git checkout synthesis
4. pip install -e .
5. pip install -e .[torch]
6. pip install -e . --upgrade
7. pip install -r references/requirements.txt
8. pip install -r requirements.txt
```

## Dataset Creation/Usage


### IndicCorp Dataset

1. Download data for the required language from here - [link](https://paperswithcode.com/dataset/indiccorp)
2. Run the ```code files present in misc_code folder accordingly``` step-by-step according to the suggested execution procedure
4. Copy the Vocab and create a new dictionary element for the new vocab set in the doctr/datasets/vocabs.py file accordingly


## Training Details

```
python references/recognition/train_pytorch.py crnn_vgg16_bn --train_txt_path TRAIN_TXT_PATH --val_txt_path VAL_TXT_PATH --vocab VOCAB_NAME --name NAME_OF_EXP --epochs 10 --font FONTS_PATH
```

The resulting models is saved in *models* dir outside the main repository

