# portfolio-display
Small Streamlit webapp to display my investment portfolio. 

Contains accompanying Python code in the file fetch_data.py, which fetches positions using the WealthSimple API. To use this, create a file named creds.txt, where the first line contains your email, the second line contains your password, and the third line contains your account number. Then, run fetch_data.py to create the file positions.txt. 

Then, to run the app, make sure that positions.txt is in the working directory and that the required libraries (pandas, yfinance, streamlit, exchangeratesapi) are available. Then, while in the same directory, type `streamlit run app.py`. 

Slight changes to the code may be necessary if stocks from different exchanges are in your portfolio, so that the yfinance library can retriece the stock price information. 
