import pandas as pd

# Input and output file paths
input_file = "US_Accidents.csv"     # Path to your CSV
output_file = "US_Accidents_Cleaned.csv"

# Read the full CSV file
print("Reading the dataset...")
df = pd.read_csv(input_file, low_memory=False)

# Remove rows with any null values
print("Removing null values...")
df.dropna(inplace=True)

# Remove duplicate rows
print("Removing duplicate rows...")
df.drop_duplicates(inplace=True)

# Save cleaned data
df.to_csv(output_file, index=False)

print(f"Cleaning complete. Cleaned dataset saved as {output_file}")
print(f"Final dataset shape: {df.shape}")