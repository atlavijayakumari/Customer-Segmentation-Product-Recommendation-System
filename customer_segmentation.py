# customer_segmentation_step3.py

import pandas as pd
from sklearn.cluster import KMeans

# Load prepared customer data
df = pd.read_csv("customer_features.csv")

# Select features for segmentation
X = df[['TotalSpend', 'PurchaseCount']]

# Apply KMeans Clustering (grouping)
kmeans = KMeans(n_clusters=3, random_state=0)
df['Segment'] = kmeans.fit_predict(X)

# Show segmented customers
print("\nCustomer Segments:")
print(df.head())

