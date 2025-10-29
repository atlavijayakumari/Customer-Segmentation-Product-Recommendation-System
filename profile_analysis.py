import pandas as pd

# Load segmented customer data
df = pd.read_csv("segmented_customers.csv")

# Count customers in each segment
count = df['Segment'].value_counts()

# Find average spend and purchase count
summary = df.groupby('Segment')[['TotalSpend', 'PurchaseCount']].mean()

# Find most common category
category = df.groupby('Segment')['PreferredCategory'].agg(lambda x: x.mode()[0])

# Combine all results
profile = pd.concat([count, summary, category], axis=1)
profile.columns = ['NumCustomers', 'AvgSpend', 'AvgPurchase', 'TopCategory']

# Show and save results
print(profile)
profile.to_csv("segment_profile_summary.csv")
print("\nProfile summary saved!")
