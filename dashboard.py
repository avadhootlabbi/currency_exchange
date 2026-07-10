import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Currency Converter", layout="centered")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .convert-btn {
        background-color: #00b140;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 18px 35px;
        font-size: 22px;
        font-weight: 700;
        cursor: pointer;
        width: 100%;
    }
    .convert-btn:hover {
        background-color: #009933;
    }
    .currency-select {
        width: 100%;
        font-size: 20px;
        padding: 12px;
        border-radius: 12px;
        border: 2px solid #444;
        background-color: #2b2f36;
        color: white;
    }
    .amount-input {
        font-size: 22px;
        padding: 12px;
        border-radius: 12px;
        border: 2px solid #444;
        background-color: #2b2f36;
        color: white;
        width: 100%;
    }
    h1 {
        font-size: 76px;
        font-weight: 800;
        color: #00b140;
        text-align: center;
    }
    p {
        font-size: 20px;
        color: #dfe6e9;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("<h1>💱 Currency Converter</h1>", unsafe_allow_html=True)
st.markdown("<p>Convert currencies at real-time exchange rates</p>", unsafe_allow_html=True)

# ------------------ CONVERTER BOX ------------------
st.markdown("<div class='converter-box'>", unsafe_allow_html=True)

# Input amount
amount = st.number_input("Amount", min_value=1.0, value=1000.0, step=1.0, format="%.2f")

# Currency dropdowns
col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("From Currency", ["USD", "INR", "EUR", "GBP", "JPY", "AUD"], index=0)
with col2:
    to_currency = st.selectbox("To Currency", ["INR", "USD", "EUR", "GBP", "JPY", "AUD"], index=1)

# Convert button
if st.button("Convert 💱"):
    pair = f"{from_currency}{to_currency}=X"
    data = yf.download(pair, period="7d", interval="1h")
    if not data.empty:
        rate = data["Close"].iloc[-1]
        rate = rate.item() if hasattr(rate, "item") else float(rate)
        converted_amount = amount * rate

        st.success(f"💱 {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        st.info(f"Mid-market exchange rate: 1 {from_currency} = {rate:.4f} {to_currency}")
