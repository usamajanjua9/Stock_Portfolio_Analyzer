# 📌 Import necessary libraries
import streamlit as st  # For creating the interactive UI
import pandas as pd  # For handling financial data

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 📌 App Title and Description
st.title("📈 Stock Portfolio Analyzer")  # App heading
st.write("Upload your stock transaction CSV file to analyze your investment portfolio.")  # Short description

# 📌 File uploader for user to upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check if a file is uploaded
if uploaded_file:
    # 📌 Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # 📌 Display the first few rows of the uploaded data
    st.subheader("📊 Uploaded Data Preview")
    st.write(df.head())  # Show first 5 rows of the dataset

    # 📌 Portfolio Summary Section
    st.subheader("📌 Portfolio Summary")

    # Check if required columns are present in the dataset
    required_columns = ["Stock", "Quantity", "Buy Price", "Current Price"]
    if all(col in df.columns for col in required_columns):

        # 📌 Calculate total investment, current value, and profit/loss
        df["Investment"] = df["Quantity"] * df["Buy Price"]  # Total money spent on each stock
        df["Current Value"] = df["Quantity"] * df["Current Price"]  # Current market value of stocks
        df["Profit/Loss"] = df["Current Value"] - df["Investment"]  # Profit or loss calculation

        # 📌 Calculate total portfolio summary
        total_investment = df["Investment"].sum()  # Sum of all investments
        total_value = df["Current Value"].sum()  # Sum of all current values
        total_profit = df["Profit/Loss"].sum()  # Sum of all profits/losses

        # 📌 Display overall portfolio summary using Streamlit metrics
        st.metric("💰 Total Investment (PKR)", f"{total_investment:,.2f}")  # Show total money invested
        st.metric("📈 Current Portfolio Value (PKR)", f"{total_value:,.2f}")  # Show total portfolio value
        st.metric("📊 Total Gain/Loss (PKR)", f"{total_profit:,.2f}", delta=f"{total_profit:,.2f}")  # Show gain/loss

        # 📌 Display performance of individual stocks
        st.subheader("📌 Stock Performance Summary")
        st.write(df[["Stock", "Investment", "Current Value", "Profit/Loss"]])  # Show per-stock performance

        # 📌 Allow user to select a stock for analysis
        st.subheader("🔍 Analyze Individual Stocks")
        selected_stock = st.selectbox("Choose a stock", df["Stock"].unique())  # Dropdown to select a stock
        stock_data = df[df["Stock"] == selected_stock]  # Filter data for selected stock

        # 📌 Display details of selected stock
        st.write(f"📌 **Performance of {selected_stock}**")
        st.write(stock_data[["Quantity", "Buy Price", "Current Price", "Investment", "Current Value", "Profit/Loss"]])

        # 📌 Portfolio Gain/Loss Breakdown
        st.subheader("📊 Portfolio Gain/Loss Breakdown")

        # Find stocks that made a profit
        gain_stocks = df[df["Profit/Loss"] > 0]
        # Find stocks that are at a loss
        loss_stocks = df[df["Profit/Loss"] < 0]

        # 📌 Display profitable stocks
        st.write("✅ **Profitable Stocks:**")
        st.write(gain_stocks[["Stock", "Profit/Loss"]])

        # 📌 Display loss-making stocks
        st.write("❌ **Loss-making Stocks:**")
        st.write(loss_stocks[["Stock", "Profit/Loss"]])

    else:
        # Display error if CSV format is incorrect
        st.error("❌ CSV file must contain 'Stock', 'Quantity', 'Buy Price', and 'Current Price' columns.")
