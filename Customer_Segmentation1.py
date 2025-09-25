# customer_segmentation.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load engineered features
customer_features = pd.read_csv("customer_features_prepared.csv")
print("Customer Features Loaded:\n", customer_features.head())

# 2️⃣ Select numeric features for clustering
features = customer_features[['TotalSpend', 'PurchaseFrequency']]

# 3️⃣ Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# 4️⃣ Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # 3 clusters as example
customer_features['Cluster'] = kmeans.fit_predict(scaled_features)

# 5️⃣ Analyze clusters
print("\nCluster Counts:")
print(customer_features['Cluster'].value_counts())

print("\nCluster Means:")
print(customer_features.groupby('Cluster')[['TotalSpend','PurchaseFrequency']].mean())

# 6️⃣ Visualize clusters
sns.scatterplot(
    x='PurchaseFrequency', y='TotalSpend',
    hue='Cluster', data=customer_features,
    palette='Set2', s=100
)
plt.title("Customer Segmentation")
plt.xlabel("Purchase Frequency")
plt.ylabel("Total Spend")
plt.show()

# 7️⃣ Save clustered data
customer_features.to_csv("customer_features_clustered.csv", index=False)
print("\nClustered customer features saved to 'customer_features_clustered.csv'")
