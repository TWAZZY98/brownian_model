import numpy as np
import pandas as pd
from matplotlib import pyplot as mp
import yfinance as yf
import normalmodel as nm

def main():
    print("this is the a normal model stock prediction")
      
    nam = input(f"Name of stock you want to predict ")
    time = input(f"how many months in the future do you want to predict?: ")
    
    cache={}
    def get_data(ticker):
        if ticker not in cache:
            cache[ticker] = True
            yf.download(ticker,progress=False,period="max")
        return cache[ticker]
    
    df = get_data(nam)
    print(df.iloc[-1])
    initdate = df.index[-1]- pd.DateOffset(months=int(time)) 
    dft = df.loc[df.index <= initdate, "Close"]
    def SPeriodReturn(df)->float|None:
        if df.empty:
            return None
        i=dft.iloc[-1]
        f = dft.iloc[1]
        return (f/i) -1.0
    def MPeriodReturn(df)->float:
        values = df.to_numpy()
        print(values)
        return 0.0
            
    predRet = SPeriodReturn(df)
    predPrice = dft.iloc[-1] + predRet*float(time)
    print(f"predicted return: {predRet}")
    print(f"predicted price: \n{predPrice}")
    
    
    

if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()