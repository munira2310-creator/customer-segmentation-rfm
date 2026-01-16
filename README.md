\# Customer Segmentation using RFM Analysis



\## 📌 Project Overview



This project performs \*\*customer segmentation\*\* on retail transaction data using the \*\*RFM (Recency, Frequency, Monetary)\*\* framework. The goal is to convert raw transactional data into \*\*business-ready customer insights\*\* that can support marketing strategy, customer retention, and revenue optimization.



The project follows an \*\*end-to-end analytics workflow\*\* — from data cleaning to segmentation and dashboard deployment — making it suitable for \*\*real-world business use cases\*\*.



---



\## 🎯 Business Objective



\* Identify high-value and loyal customers

\* Detect at-risk customers for retention strategies

\* Understand customer purchase behavior

\* Enable data-driven marketing and decision-making



---



\## 🛠️ Tools \& Technologies



\* \*\*Python\*\*

\* \*\*Pandas \& NumPy\*\* (Data processing)

\* \*\*Matplotlib\*\* (Exploratory visualization)

\* \*\*Streamlit\*\* (Interactive dashboard)

\* \*\*Jupyter Notebook\*\* (Analysis \& development)



---



\## 📂 Dataset Description



\*\*Source:\*\* Online Retail Transaction Data



\*\*Key Columns Used:\*\*



\* `InvoiceNo` – Unique invoice identifier

\* `InvoiceDate` – Transaction date

\* `CustomerID` – Unique customer identifier

\* `Quantity` – Items purchased

\* `UnitPrice` – Price per unit

\* `TotalAmount` – Calculated transaction value



---



\## 🧹 Data Cleaning \& Preparation



\* Removed transactions with missing `CustomerID`

\* Excluded returned or invalid orders (negative quantity or price)

\* Converted data types for accurate calculations

\* Created total transaction value (`Quantity × UnitPrice`)



These steps ensure \*\*data integrity and analytical reliability\*\*.



---



\## 📊 RFM Analysis Methodology



\### 1️⃣ Recency (R)



\* Measures how recently a customer made a purchase

\* Calculated as days since the last transaction

\* More recent customers receive higher scores



\### 2️⃣ Frequency (F)



\* Measures how often a customer purchases

\* Calculated using \*\*unique invoice count\*\* (not line items)



\### 3️⃣ Monetary (M)



\* Measures total customer spending

\* Calculated as the sum of transaction values



---



\## 🧮 RFM Scoring Logic



\* Customers are ranked and divided into \*\*quintiles (1–5)\*\*

\* Ranking is applied before binning to handle skewed retail data

\* Ensures stable and error-free quantile segmentation



Higher scores indicate \*\*stronger customer value\*\*.



---



\## 👥 Customer Segmentation Rules



| Segment           | Description                         |

| ----------------- | ----------------------------------- |

| Loyal Customers   | Recent and frequent buyers          |

| New Customers     | Recently acquired but low frequency |

| At Risk Customers | High frequency but not recent       |

| Regular Customers | Average purchase behavior           |



Segments are created using \*\*rule-based business logic\*\* for interpretability.



---



\## 📈 Dashboard (Streamlit)



The project includes an interactive \*\*Streamlit dashboard\*\* that allows users to:



\* View customer segment distribution

\* Explore RFM scores dynamically

\* Inspect customer-level data



---



\## ▶️ How to Run the Project



```bash

pip install -r requirements.txt

streamlit run app.py

```



---



\## 📁 Project Structure



```

customer-segmentation-rfm/

│

├── Customer Segmentation.ipynb

├── Customer\_Segmentation\_RFM.csv

├── app.py

├── requirements.txt

└── README.md

```



---



\## 💡 Key Takeaways



\* Demonstrates \*\*business-oriented analytics\*\*, not just coding

\* Handles real-world data challenges (skewness, duplicates)

\* Ready for GitHub portfolio, interviews, and dashboards



---



\## 👤 Author



\*\*Shirajum\*\*

Senior Principal Officer | Data Analytics Enthusiast
