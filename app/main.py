import numpy as np
import pandas as pd
from matplotlib import pyplot as mp
import normalmodel as nm
import csvdatabase as csvd
import yfinance as yf

def main():
    print("this is the a normal model stock prediction")
      
    nam = input(f"Name of stock you want to predict ")
    time = input(f"how many months in the future do you want to predict?: ")
        
    df = csvd.get_data(nam)
    df["Date"]= pd.to_datetime(df["Date"])
    lastdate = df['Date'].iloc[-1]
    initdate = lastdate- pd.DateOffset(months=int(time)) 
    dft = df[df["Date"]>=initdate]
    print(dft)
    def SPeriodReturn(df)->float|None:
        if df.empty:
            return None
        i=dft['Close'].iloc[0]
        f = dft['Close'].iloc[-1]
        print(type(i), type(f))
        return (f/i) -1.0
    def MPeriodReturn(df)->float:
        values = df.to_numpy()
        print(values)
        return 0.0
            
    predRet = SPeriodReturn(df)
    predPrice = dft['Close'].iloc[-1] + predRet*float(time)
    print(f"predicted return: {predRet*100}%")
    print(f"predicted price: \n{predPrice}")
    
    
    

if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()