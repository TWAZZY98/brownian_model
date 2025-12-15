import numpy as np
import pandas as pd
from matplotlib import pyplot as mp
import yfinance as yf

def main():
    print("this is the brownian simulation")
      
    nam = input(f"Name of stock you want to predict ")
    time = input(f"how many months in the future do you want to predict?: ")

    try:
        df = yf.download(nam, period=f"{time}mo", progress=False)

        if df.empty:
            print(f"{nam}: No data (404). Skipped.")

        print(f"{nam}: OK")

    except Exception as e:
        print(f"{nam}: Failed ({e})")
    
    def SPeriodReturn(initial, final)->float:
        return (final/initial) -1.0
            
    i=df['Close'].iloc[-1]
    f = df['Close'].iloc[1]
    predRet = SPeriodReturn(i,f)
    predPrice = i + predRet*float(time)
    print(f"predicted return: {predRet}")
    print(f"predicted price: \n{predPrice}")
   #print(df)
        
        
    
    


if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()