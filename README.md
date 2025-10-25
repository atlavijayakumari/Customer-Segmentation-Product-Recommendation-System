****Vijaya Kumari Atla**

🧾 **Final Report – Flipkart Data Science Internship Project**

---

### 🧩 **Project Title:**  
**Customer Segmentation & Product Recommendation System**

---

### 🎯 **Objective:**  
To analyze customer purchase history, segment buyers into meaningful groups, and build a recommendation system that suggests relevant products to each customer segment — enabling smarter marketing and personalized shopping experiences.

---

### 🧰 **Tools & Libraries Used:**  
- **Python:** Data processing & analysis  
- **pandas:** Cleaning, aggregation, feature creation  
- **numpy:** Numerical operations  
- **matplotlib & seaborn:** Data visualization  
- **scikit-learn:** Clustering & modeling  
- **surprise:** Product recommendation algorithms  
- **VS Code:** Development environment  
- **GitHub:** Version control & submission  

---

### 📂 **Data Source Used:**  
`sample_transactions.csv` – Provided by Flipkart  

**Columns:**  
`CustomerID`, `ProductID`, `Category`, `PurchaseAmount`, `PurchaseDate`

---

### 🧹 **Data Cleaning Summary:**  
- Removed missing values and duplicates  
- Converted `PurchaseDate` to datetime format  
- Standardized column names and product categories  
- Prepared dataset for feature engineering  

---

### ⚙️ **Feature Engineering:**  
Derived key customer metrics:  
- **Total Spend** – Total amount spent  
- **Purchase Frequency** – Number of transactions  
- **Average Purchase Value** – Mean spend per order  
- **Preferred Category** – Most purchased product type  

🗂️ Output file: `customer_features_prepared.csv`

---

### 🤖 **Customer Segmentation:**  
- Scaled data using `StandardScaler`  
- Applied **K-Means Clustering** → Identified 3 distinct segments  

**Clusters Identified:**  
1️⃣ High Spenders  
2️⃣ Moderate Buyers  
3️⃣ Low Spenders  

---

### 🔍 **Profile Analysis:**  
| Cluster | Spending Pattern | Preferred Category |
|----------|------------------|--------------------|
| 0 | High-value buyers | Electronics |
| 1 | Moderate spenders | Fashion |
| 2 | Budget-conscious | Groceries |

---

### 💡 **Recommendation System:**  
Built a **Collaborative Filtering Model** using the **Surprise library** (KNNBasic algorithm).  

**Steps:**  
- Used `CustomerID` and `ProductID` interaction matrix  
- Computed similarity scores between users  
- Predicted products each user is likely to purchase next  

**Top 3 Recommendations (example):**  
| Customer Segment | Recommended Products |
|------------------|----------------------|
| High Spenders | Smartphones, Smartwatches, Laptops |
| Moderate Buyers | Clothing, Footwear, Accessories |
| Low Spenders | Groceries, Daily Essentials, Home Items |

📦 Output file: `recommendations_output.csv`

---

### 📊 **Visualizations Created:**  
- 🥧 Pie Chart – Customer Segment Distribution  
- 📊 Bar Chart – Average Spend by Cluster  
- 📈 Line Chart – Category Preference Trends  
- 📉 Recommendation Accuracy Curve  

🖼️ All visuals saved in the `outputs/` folder  

---

### 💻 **How to Run This Project:**  
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scikit-surprise
python cleaning.py
python feature_engineering.py
python customer_segmentation.py
python recommendation_system.py
python visualization.py
