from tqdm import tqdm

# Define the input and output file paths
input_file_path = './../../data/as.txt'
output_file_path = './../../processed/as_words.txt'

# Function to process a line and extract words
def process_line(line):
    # Split the line into words based on whitespace
    words = line.split()
    return words

# Open the input and output files
with open(input_file_path, 'r', encoding='utf-8') as input_file, open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Process the file line by line
    for line in tqdm(input_file):
        # Extract words from the line
        words = process_line(line)
        
        # Write each word to the output file on separate lines
        for word in words:
            output_file.write(word + '\n')

print("Data extraction and storage complete.")
