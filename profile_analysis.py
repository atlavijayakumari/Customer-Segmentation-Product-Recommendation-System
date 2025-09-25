# profile_analysis.py
import pandas as pd

# 1️⃣ Load clustered customer data
customer_features = pd.read_csv("customer_features_clustered.csv")
print("Clustered Customer Features Loaded:\n", customer_features.head())

# 2️⃣ Number of customers per cluster
cluster_counts = customer_features['Cluster'].value_counts().reset_index()
cluster_counts.columns = ['Cluster', 'NumCustomers']
print("\nNumber of Customers per Cluster:\n", cluster_counts)

# 3️⃣ Average spend & purchase frequency per cluster
cluster_summary = customer_features.groupby('Cluster')[['TotalSpend','PurchaseFrequency']].mean().reset_index()
print("\nCluster Summary (Average Spend & Frequency):\n", cluster_summary)

# 4️⃣ Most preferred category per cluster
cluster_category = customer_features.groupby('Cluster')['PreferredCategory'].agg(lambda x: x.mode()[0]).reset_index()
cluster_category.rename(columns={'PreferredCategory': 'MostPreferredCategory'}, inplace=True)
print("\nMost Preferred Category per Cluster:\n", cluster_category)

# 5️⃣ Combine all cluster info
cluster_profile = cluster_counts.merge(cluster_summary, on='Cluster')\
                                .merge(cluster_category, on='Cluster')
print("\nCluster Profile:\n", cluster_profile)

# 6️⃣ Save cluster profile to CSV
cluster_profile.to_csv("cluster_profile_summary.csv", index=False)
print("\nCluster profile saved to 'cluster_profile_summary.csv'")
