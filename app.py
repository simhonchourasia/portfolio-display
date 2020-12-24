import json
import pandas as pd
import yfinance as yf
import streamlit as st
from exchangeratesapi import Api


with open("positions.txt") as f:
    data = json.load(f)
f.close()

positions = {}
for p in data['positions']:
    name = p['stock']['name']
    symbol = p['stock']['symbol']
    quantity = p['quantity']
    currency = p['currency']
    positions[name] = {'symbol': symbol, 'quantity': quantity, 'currency': currency}


st.write("""
# My Investment Portfolio

Shows how my portfolio is doing over time, mainly using the WealthSimple and Yahoo Finance APIs. Created using Streamlit. 
""")


# Helper function to find the dataframe for a position
def get_dataframe(position):
    ticker = position['symbol']
    if position['currency'] == 'CAD':
        ticker += '.TO'
    ticker_data = yf.Ticker(ticker)
    ticker_df = ticker_data.history(period='3mo', interval='1h').Close
    ticker_df *= position['quantity']
    if position['currency'] == 'USD':
        api = Api() # using exchangeratesapi
        exchange_rate = api.get_rates('USD')['rates']['CAD']
        ticker_df *= exchange_rate
    return ticker_df


# Create line chart
portfolio = get_dataframe(positions['Vanguard S&P 500 Index ETF'])
for p in positions:
    print(positions[p])
    if p != 'Vanguard S&P 500 Index ETF':
        portfolio = portfolio.add(get_dataframe(positions[p]))

st.line_chart(portfolio)


# Show positions
df_positions = pd.DataFrame.from_dict(positions)
st.write(df_positions)

# Show summary
initial_amount_invested = 3000 - 166.96 # Hardcoded
portfolio_value = round(portfolio[-1], 2)
gain = round((portfolio_value - initial_amount_invested), 2)
st.header("Initial amount invested: $" + str(initial_amount_invested))
st.header("Current portfolio value: $" + str(portfolio_value))
st.header("Total gain: $" + str(gain))
