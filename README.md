Final Submission — Flipkart Task 2: Customer Segmentation and Product Recommendation

1. Importing the Dataset

The dataset is provided in the task as sample_transactions.csv.

It includes the following fields:

CustomerID

ProductID

Category

PurchaseAmount

PurchaseDate



---

2. Libraries Used

pandas

numpy

matplotlib

scikit-learn


(Install them using: pip install pandas numpy matplotlib scikit-learn)


---

3. Programming Details

Language: Python

Environment: VS Code

Submission Platform: GitHub



---

4. Cleaning Script (cleaning.py)

This script prepares the raw dataset for analysis.

Removes duplicate entries using the drop function.

Handles missing values by replacing them with suitable values (like 0 or mean/median).

The cleaned file becomes the base for feature creation and segmentation.



---

5. Feature Engineering (feature_engineering.py)

In this part, additional customer-based features are created:

Total spending per customer

Number of purchases

Most preferred product category
These new columns help in analyzing customer behavior more effectively.



---

6. Customer Segmentation (customer_segmentation.py)

Using K-Means clustering, customers are divided into 3 segments based on spending and purchase count:

Cluster 0: High Spenders (Loyal Customers)

Cluster 1: Medium Spenders (Average Buyers)

Cluster 2: Low Spenders (Occasional Buyers)


This helps identify how different customer types behave.


---

7. Profile Analysis (profile_analysis.py)

This step summarizes each segment’s characteristics:

Number of customers in each group

Average purchase amount

Most popular category
It gives a clear view of how each cluster differs in buying habits.



---

8. Recommendation System (recommendation_system.py)

Based on the profile analysis:

High spenders are suggested premium products

Average buyers get mid-range items

Occasional buyers are recommended discounted or budget products


This helps improve personalized marketing strategies.


---

9. Visualization (visualization.py)

To make insights more understandable:

Pie chart: shows the proportion of customers in each segment.

Bar chart: compares total spend and purchase count between groups.



---

10. How to Run the Project

Step 1: Keep All Files Together

Place these files in one folder:

cleaning.py  
feature_engineering.py  
customer_segmentation.py  
profile_analysis.py  
recommendation_system.py  
visualization.py  
sample_transactions.csv

Step 2: Install Libraries

Run these commands:

pip install pandas numpy matplotlib scikit-learn

Step 3: Execute Scripts

Run each file one by one in order:

1️⃣ cleaning.py  
2️⃣ feature_engineering.py  
3️⃣ customer_segmentation.py  
4️⃣ profile_analysis.py  
5️⃣ recommendation_system.py  
6️⃣ visualization.py


---

✅ Conclusion:
This project helps Flipkart understand customer behavior through segmentation and product recommendations. It enables better targeting, improved customer satisfaction, and increased sales efficiency.
