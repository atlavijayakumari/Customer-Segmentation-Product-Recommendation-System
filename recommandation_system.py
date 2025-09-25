# recommendation_system.py
import pandas as pd

# 1️⃣ Load clustered customer features and original transactions
customer_clusters = pd.read_csv("customer_features_clustered.csv")
transactions = pd.read_csv("sample_transactions.csv")

# 2️⃣ Create a product list for each category
category_products = transactions.groupby('Category')['ProductID'].unique().to_dict()
print("Category to Products Mapping:\n", category_products)

# 3️⃣ Recommend products based on preferred category of each cluster
def recommend_products(row, category_products):
    category = row['PreferredCategory']
    # Return the list of products in that category
    return list(category_products.get(category, []))

# 4️⃣ Apply recommendations for each customer
customer_clusters['RecommendedProducts'] = customer_clusters.apply(
    recommend_products, axis=1, category_products=category_products
)

# 5️⃣ Preview recommendations
print("\nCustomer Recommendations:\n", customer_clusters[['CustomerID','Cluster','PreferredCategory','RecommendedProducts']])

# 6️⃣ Save recommendations to CSV
customer_clusters.to_csv("customer_recommendations.csv", index=False)
print("\nCustomer recommendations saved to 'customer_recommendations.csv'")
