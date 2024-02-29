import pandas as pd

# Define the input and output file paths
input_file_path = './../../processed/as_filtered.txt'
output_file_path = './../../processed/as_filtered_duplicates.txt'

# Read the input file into a DataFrame
df = pd.read_csv(input_file_path, header=None, names=['word'])

# Remove duplicate words
df = df.drop_duplicates()

# Save the unique words to the output file
df.to_csv(output_file_path, header=False, index=False, sep='\n')

print("Duplicate words removed and stored in output file.")
