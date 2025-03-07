
# 📈 Stock Portfolio Analyzer

A **Streamlit-based web application** that allows users to **upload stock transaction data** and gain insights into **total investment, current portfolio value, and profit/loss**.

This tool is perfect for **individual investors, traders, and finance students** who want to **analyze stock portfolios easily**.


[Run](https://stockportfolioanalyzer.streamlit.app/)!

---

## 🚀 Features
✔ **Upload a CSV file** containing stock transactions  
✔ **Calculate total investment, current value, and gain/loss**  
✔ **Analyze individual stock performance**  
✔ **Separate profitable and loss-making stocks**  
✔ **Download processed financial data as CSV**  
✔ **User-friendly, interactive interface built with Streamlit**  

---

## 📂 Sample CSV File Format
Your **CSV file** should have the following **columns**:

| Stock | Quantity | Buy Price | Current Price |
|--------|---------|-----------|--------------|
| AAPL  | 10      | 175       | 190          |
| TSLA  | 5       | 700       | 650          |
| MSFT  | 8       | 310       | 320          |
| GOOGL | 3       | 2800      | 2900         |
| AMZN  | 7       | 3500      | 3600         |

📥 **[Download Sample CSV](https://github.com/usamajanjua9/Stock_Portfolio_Analyzer/blob/main/file.csv)** 

---

## 💻 Installation & Usage

### **1️⃣ Install Dependencies**
Before running the application, **install the required dependencies** using:
```sh
pip install streamlit pandas
```

### **2️⃣ Run the Application**
To start the **Streamlit app**, run the following command:
```sh
streamlit run Stock_Portfolio_Analyzer.py
```

### **3️⃣ Upload Your CSV File**
- Click on **"Upload CSV File"** in the app  
- Select your **stock transaction CSV file**  
- View the **portfolio summary, profit/loss breakdown, and individual stock performance**  

### **4️⃣ View Processed Data**
- The app will generate **data** containing:
  - Investment details
  - Current portfolio values
  - Gain/Loss per stock  

---

## 📌 Project Structure
```
📁 stock-portfolio-analyzer
│── Stock_Portfolio_Analyzer.py   # Streamlit application script
│── sample_stock_transactions.csv  # Sample CSV file for testing
│── requirements.txt               # List of dependencies
│── README.md                      # Project documentation
```

---

## 🔥 Future Enhancements
🚀 **Add interactive graphs** using Plotly or Matplotlib  
🚀 **Fetch real-time stock prices** via API (e.g., Alpha Vantage, Yahoo Finance)  
🚀 **Enable multi-portfolio support** for different investment strategies  

---

## 🛠 Technologies Used
✔ **Python** - Backend processing  
✔ **Pandas** - Financial data handling  
✔ **Streamlit** - Interactive user interface  


---

## 📜 License
This project is licensed under the **MIT License**.

---

### 🎯 **Now you can track and analyze your stock investments like a pro! 🚀**
```

