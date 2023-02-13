import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyzer

    Shown are the stock prices of Apple
    
    """
    
)

ticker_symbol = st.text_input(
                        "Enter Stock Symbol", 
                        "AAPL",
                        key="placeholder"
)

#ticker_symbol = "AAPL"

col1, col2 = st.columns(2)

with col1:
    start_date=st.date_input("Input Starting Date",
                datetime.date(2019,1,1))
with col2:
    end_date = st.date_input("Input Ending Date",
                datetime.date(2022,12,31))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="id",
                                start=f"{start_date}",
                                end=f"{end_date}")
st.dataframe(ticker_df)

## Charts
st.write("""
## Daily Closing Price Chart
""")

st.line_chart(ticker_df.Close)