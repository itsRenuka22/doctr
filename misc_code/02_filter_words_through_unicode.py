from tqdm import tqdm

# Define the input and output file paths
input_file_path = './../../processed/as_words.txt'
output_file_path = './../../processed/as_filtered.txt'


# Unicode range for language script (Bengali block)
language_unicode_range = (0x0980, 0x09FF)

# Function to check if a character falls within the language Unicode range
def is_language_character(char):
    char_code = ord(char)
    return language_unicode_range[0] <= char_code <= language_unicode_range[1]

# Initialize a list to store language words
language_words = []

# Open the input file
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    # Process the file line by line
    for line in input_file:
        words = line.split()
        for word in tqdm(words):
            # Check each character in the word
            if all(is_language_character(char) for char in word):
                language_words.append(word)

# Write language words to the output file
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for word in language_words:
        output_file.write(word + '\n')

print("language word extraction and storage complete.")
