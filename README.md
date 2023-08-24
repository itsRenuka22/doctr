# INDIC DocTR





# Installation

```
1. git clone https://github.com/iitb-research-code/doctr.git
2. cd doctr
3. git checkout indic
4. pip install -e .
5. pip install -e .[torch]
6. pip install -e . --upgrade
7. pip install -r references/requirements.txt
```

# Dataset Creation/Usage

## Indic Handwritten Text Recognition

### IIIT-Indic words dataset

1. Download data for the required language from here - [link](https://cvit.iiit.ac.in/research/projects/cvit-projects/iiit-indic-hw-words)
2. Run the ```python scripts/iiit_indic_words.py --data_dir PATH_TO_THE_DATA``` to convert the data into trainable format as required for DocTR
3. With the above code, vocab is printed in terminal and also the json files are created
4. Copy the Vocab and create a new dictionary element for the new vocab set in the doctr/datasets/vocabs.py file accordingly


## Printed Text Recogniton


# Training Details

```
python references/recognition/train_pytorch_ihtr.py crnn_vgg16_bn --train_path DATA_DIR --epochs 10 -b 1024 --vocab VOCAB --device 0
```

The resulting models is saved in *models* dir outside the main repository


# Inference Details

Run ```python scrpts/ihtr_inference.py``` accordingly to get inference on detection models and recogniton models available
