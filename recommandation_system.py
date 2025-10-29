#step 5
# recommendation_system.py
import pandas as pd

# Load customer data
df = pd.read_csv("segmented_customers.csv")

# Recommendation logic based on segment
def recommend(segment):
    if segment == 0:
        return "Recommend Premium Products"
    elif segment == 1:
        return "Recommend Mid-Range Offers"
    else:
        return "Recommend Budget-Friendly Deals"

# Apply recommendations
df['Recommendation'] = df['Segment'].apply(recommend)

# Show some results
print("Sample Recommendations:\n")
print(df[['CustomerID', 'Segment', 'Recommendation']].head())

# Save to CSV
df.to_csv("customer_recommendations.csv", index=False)
print("\nRecommendations saved to 'customer_recommendations.csv'")
