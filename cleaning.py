import pandas as pd

# 1️⃣ Load dataset
df = pd.read_csv("sample_transactions.csv")

# 2️⃣ Basic info
print("Dataset shape:", df.shape)
print(df.head())
print("\nMissing values:\n", df.isnull().sum())

# 3️⃣ Handle missing values
for col in df.select_dtypes(include='number'):
    df[col] = df[col].fillna(df[col].median())  # assign back instead of inplace

for col in df.select_dtypes(include='object'):
    df[col] = df[col].fillna(df[col].mode()[0])  # assign back instead of inplace

# 4️⃣ Remove duplicates
df = df.drop_duplicates()

# 5️⃣ Create basic customer features
customer_features = df.groupby('CustomerID').agg({
    'PurchaseAmount': 'sum',           # total spend
    'ProductID': 'count',              # purchase frequency
    'Category': lambda x: x.mode()[0]  # preferred category
}).reset_index()

# 6️⃣ Preview cleaned features
print("\nCustomer Features:")
print(customer_features.head())

# 7️⃣ Save prepared features
customer_features.to_csv("customer_features_prepared.csv", index=False)
print("\nPrepared features saved to 'customer_features_prepared.csv'")
