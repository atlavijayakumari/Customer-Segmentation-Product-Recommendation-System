# customer_segmentation.py

# Step 1: Import necessary library
import pandas as pd

# Step 2: Load CSV file
df = pd.read_csv('sample_transactions.csv')  # CSV must be in the same folder

# Step 3: View first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: Check dataset info
print("\nDataset information:")
print(df.info())
