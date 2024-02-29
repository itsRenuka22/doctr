# Define the input file path
input_file_path = './../../processed/as_filtered_duplicates.txt'

# Create an empty set to store unique characters
unique_characters = set()

# Open the input file and process each line
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    for line in input_file:
        # Remove whitespace and newline characters
        line = line.strip()
        # Add each character to the set
        unique_characters.update(line)

# Convert the set to a sorted list (if needed)
unique_characters_list = sorted(list(unique_characters))

# Print or use the unique characters
print("Unique characters:", unique_characters_list)


print("\n", ''.join(unique_characters_list), "\n")

print("Store the above vocab string in the vocabs.py of the doctr/datasets/vocabs.py file accordingly")