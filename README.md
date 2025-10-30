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
 In this we have to apply some algorithms and find the insights like favourite product of a
 customer and favourite catogiry like features to analyze.


9.profile_analysis.py :
  Based upon the customer segmentation we make the groups by merging the similar data.
  A group is a collection of customers based upon the buying behaviour like
  having similar product, purchasing customers .

  Based on all of these insights and patterns we have to analyze the profile of thet particular segment.


10.recommendation_system.py :
  Based upon the analysis we recommend the upcoming buying products to the customers.
  For example,
     -We suggest premium products for the high spenders
     -we suggest medium products for te average spenders
     -and suggest discounts and low cost products to the occasional customers


11.visualization.py:
  Instead of showing numbers it is better to show the numbers in graphical representation.
  So,we have to show customer segmentation in a graphical representation.
  *pie chart is used to show the segment size(no.of customes in a segment)
  *bar chart is used to represent comparison between the total spend and the purchase count.



12.How to run the project:
   

Step 1: Project Setup

Keep all project files in the same folder:

cleaning.py  
feature_engineering.py  
customer_segmentation.py  
profile_analysis.py  
recommendation_system.py  
visualization.py  
sample_transactions.csv


Step 2: Install Required Libraries

If using VS Code or pc:

pip install pandas 
pip install numpy 
pip install matplotlib 
pip install scikit-learn


💻 Step 3: Run Each Script in Order

