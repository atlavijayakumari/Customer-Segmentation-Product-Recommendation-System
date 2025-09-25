# visualizations.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Load clustered customer features with recommendations
customer_clusters = pd.read_csv("customer_recommendations.csv")
print("Customer Clusters Loaded:\n", customer_clusters.head())

# Set seaborn style
sns.set(style="whitegrid")

# 2️⃣ Segment Sizes: Number of Customers per Cluster
plt.figure(figsize=(6,4))
sns.countplot(x='Cluster', data=customer_clusters, palette='Set2')
plt.title("Number of Customers per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Number of Customers")
plt.show()

# 3️⃣ Spending Patterns: Average Total Spend per Cluster
plt.figure(figsize=(6,4))
sns.barplot(x='Cluster', y='TotalSpend', data=customer_clusters, palette='Set2')
plt.title("Average Total Spend per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Total Spend")
plt.show()

# 4️⃣ Purchase Frequency: Average Purchases per Cluster
plt.figure(figsize=(6,4))
sns.barplot(x='Cluster', y='PurchaseFrequency', data=customer_clusters, palette='Set2')
plt.title("Average Purchase Frequency per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Purchase Frequency")
plt.show()

# 5️⃣ Top Recommendations: Number of Products Recommended per Cluster
# Convert string representation of list to actual list
customer_clusters['RecommendedProductsList'] = customer_clusters['RecommendedProducts'].apply(lambda x: eval(x))
top_products = customer_clusters.groupby('Cluster')['RecommendedProductsList'].apply(lambda x: x.iloc[0]).reset_index()
top_products['NumProducts'] = top_products['RecommendedProductsList'].apply(len)

plt.figure(figsize=(6,4))
sns.barplot(x='Cluster', y='NumProducts', data=top_products, palette='Set2')
plt.title("Number of Recommended Products per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Number of Products")
plt.show()

# Optional: print top products per cluster
print("\nTop Recommended Products per Cluster:\n")
for i, row in top_products.iterrows():
    print(f"Cluster {row['Cluster']}: {row['RecommendedProductsList']}")
