import os
import yfinance as yf

csv_folder = 'csvfolder'
atickers = []
    
def get_data(ticker):
    down = None
    if ticker not in atickers:
        down = update_ticker_data(ticker)

    else:
        print(f"do you want to update {ticker} data? y-> Yes, n-> no")
        dec = input()
        dec = dec.lower()
        if dec.find("y"):
            down = update_ticker_data(ticker)
            
    return down

def update_ticker_data(ticker):
        filename = f"{ticker}.csv"
        fullpath = os.path.join(csv_folder,filename)
        down = yf.download(ticker,progress=False,period="max")
        down.to_csv(fullpath,index=False)
        return down