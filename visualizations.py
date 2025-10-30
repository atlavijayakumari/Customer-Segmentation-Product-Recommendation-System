# visualization
# Step6
import pandas as pd
import matplotlib.pyplot as plt

# Load segmented data
df = pd.read_csv("segmented_customers.csv")

# Pie chart – segment size
segment_counts = df['Segment'].value_counts()
plt.pie(segment_counts, labels=segment_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Customer Segment Distribution")
plt.show()

# Bar chart – average spending per segment
avg_spend = df.groupby('Segment')['TotalSpend'].mean()
avg_spend.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Average Spending per Segment")
plt.ylabel("Total Spend")
plt.show()

# Bar chart – average purchase frequency per segment
avg_purchase = df.groupby('Segment')['PurchaseCount'].mean()
avg_purchase.plot(kind='bar', color=['orange', 'lightblue', 'violet'])
plt.title("Average Purchase Frequency per Segment")
plt.ylabel("Purchase Count")
plt.show()
