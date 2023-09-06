import unicodedata
import sys
sys.path.append("/home/kunal/Dev/IITB/english-hindi")
from doctr.datasets import VOCABS
filename="HindiEnglishWordsCorpus.txt" #input file name which contains list of words

corpusString = open(filename, "r", encoding="utf-8").read()

#vocabs = "".join(list(set(corpus)))

#print("vocabs: ", vocabs)


vocabString=VOCABS["hinglish"]

vocab=x=[i for i in vocabString]
print("vocab", vocab)

corpus =corpusString.split()

print ("corpus type", type(corpus) )

print ("corpus:\n", corpus[10000:10005] )

updated_corpus = []
ood_corpus = []

#unicodedata.normalize("NFKD", string_)

for word in corpus:
    #word=unicodedata.normalize("NFKD", word) #print("word", word)
    valid = True
    for char in word:
        if char not in vocab:
            #print("char not in vocab",char)
            valid = False
            break
    if valid:
        updated_corpus.append(word)
    else:
        ood_corpus.append(word)

# Printing the results
print("Original Corpus", len(corpus))
print("Updated Corpus:", len(updated_corpus))
print("OOD Corpus:", len(ood_corpus))

filename = "english_hindi_Compliant.txt"

# Open the file in write mode with UTF-8 encoding
with open(filename, "w", encoding="utf-8") as file:
    # Iterate through the list and write each string to the file
    for item in updated_corpus:
        file.write(item + "\n")  # Add a newline after each string


filename1 = "english_hindi_NonComp.txt"

# Open the file in write mode with UTF-8 encoding
with open(filename1, "w", encoding="utf-8") as file:
    # Iterate through the list and write each string to the file
    for item in ood_corpus:
        file.write(item + "\n")  # Add a newline after each string

filename2="english_hindi_Compliant.txt" #input file name which contains list of words

mycorpus = open(filename2, "r", encoding="utf-8").read()

myvocabs = "".join(list(set(mycorpus)))

print("myvocabs: ", myvocabs)

print(set(myvocabs).difference(set(vocabString)))





