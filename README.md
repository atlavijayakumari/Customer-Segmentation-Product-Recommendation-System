**Vijaya Kumari Atla**

🧾 **Final Report – Flipkart Data Science Internship Project**

---

### 🧩 **Project Title:**  
**Customer Segmentation & Product Recommendation System**

---

### 🎯 **Objective:**  
To analyze customer purchase history, segment buyers into meaningful groups, and create a recommendation engine that suggests relevant products to each segment — supporting data-driven marketing strategies.

---

### 🧰 **Tools & Libraries Used:**  
- **Python:** Data processing & analysis  
- **pandas:** Cleaning, aggregation, feature creation  
- **numpy:** Numerical operations  
- **matplotlib & seaborn:** Data visualization  
- **scikit-learn:** Clustering & modeling  
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

### 📊 **Visualizations Created:**  
- 🥧 Pie Chart – Customer Segment Distribution  
- 📊 Bar Chart – Average Spend by Cluster  
- 📈 Line Chart – Category Preference Trends  

🖼️ All visuals saved in the `outputs/` folder  

---

### 💻 **How to Run This Project:**  
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
python cleaning.py
python feature_engineering.py
python customer_segmentation.py
python visualization.py
