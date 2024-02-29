import pandas as pd
from sklearn.model_selection import train_test_split

# Define the input file path and the desired validation split ratio
input_file_path = './../../processed/as_filtered_duplicates.txt'
validation_split_ratio = 0.2  # Adjust as needed (e.g., 0.2 for an 80-20 split)

# Read the dataset from the text file into a DataFrame
df = pd.read_csv(input_file_path, header=None, names=['word'])

# Split the dataset into train and validation sets
train_df, val_df = train_test_split(df, test_size=validation_split_ratio, random_state=42)

# Save the train and validation sets to separate text files
train_df.to_csv('./../../processed/train.txt', header=False, index=False)
val_df.to_csv('./../../processed/val.txt', header=False, index=False)

print("Dataset split into train and validation sets.")
