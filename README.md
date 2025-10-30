Final submission for the Flipkart task-2 named "Customer segmentation and product Recommendation"
1.importing the dataset :
 *The dataset is taken from your provided task.
 *The dataset is imported by unzipping the dataset 
  "sample_transactions.csv" which contains:
   - CustomerID
   - ProductID
   - Category
   - PurchaseAmount
   - Date


2.libraries used:
 *pip install matplotlib
 *pip install pandas
 *pip install numpy


3.programming language:
 *python


 4.programming environment:
  *vs code


 5.for project submission:
   *Github


 6.cleaning.py:
  In this we've to clean the dataset by using python programming language.
  It was mainly used to remove the duplicate values and missing values.
  In the missing values we substitute 0 or 1.
  By using drop function we remove the duplicates.


7.Customer_Segmentation.py:
  In this, based on purchase Count and total spend we make 
  three clusters they are
   *High spenders : loyal customers(cluster 0)
   *Medium spenders : average buyers(cluster 1)
   *Low spenders : occasionally buyers(cluster 2)
  these are all find by knowing the 'NumCustomers', 'AvgSpend', 'AvgPurchase', 'TopCategory'.



8.feature_engineering.py :
  Based upon the customer segmentation we make the groups.
  A 
