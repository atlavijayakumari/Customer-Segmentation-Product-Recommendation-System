# feature_engineering.py
import pandas as pd

# 1️⃣ Load cleaned dataset
df = pd.read_csv("sample_transactions.csv")  # Make sure this is your cleaned CSV
print("Dataset Loaded:\n", df.head())

# 2️⃣ Total Spend per Customer
total_spend = df.groupby('CustomerID')['PurchaseAmount'].sum().reset_index()
total_spend.rename(columns={'PurchaseAmount': 'TotalSpend'}, inplace=True)
print("\nTotal Spend:\n", total_spend.head())

# 3️⃣ Purchase Frequency per Customer
purchase_freq = df.groupby('CustomerID')['ProductID'].count().reset_index()
purchase_freq.rename(columns={'ProductID': 'PurchaseFrequency'}, inplace=True)
print("\nPurchase Frequency:\n", purchase_freq.head())

# 4️⃣ Preferred Category per Customer
preferred_category = df.groupby('CustomerID')['Category'].agg(lambda x: x.mode()[0]).reset_index()
preferred_category.rename(columns={'Category': 'PreferredCategory'}, inplace=True)
print("\nPreferred Category:\n", preferred_category.head())

# 5️⃣ Merge all features into one dataframe
customer_features = total_spend.merge(purchase_freq, on='CustomerID')\
                               .merge(preferred_category, on='CustomerID')
print("\nCustomer Features Combined:\n", customer_features.head())

# 6️⃣ Save the prepared features
customer_features.to_csv("customer_features_prepared.csv", index=False)
print("\nCustomer features saved to 'customer_features_prepared.csv'")
