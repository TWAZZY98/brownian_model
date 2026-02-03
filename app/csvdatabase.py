import os
import yfinance as yf
import pandas as pd
import json
from datetime import date
import numpy as np

json_file_path = 'data.json'
csv_folder = 'csvfolder'

os.makedirs(csv_folder, exist_ok=True)
#load json create a data json if it doesnt exits
#else load the atickers to the data json
#if file is corrupted change the data json to empty
def _load_json():
    global atickers
    
    if not os.path.exists(json_file_path):
        with open(json_file_path,"w") as file:
            json.dump({},file)
            atickers = {}
        return
    try:
        with open(json_file_path,"r") as file:
            atickers = json.load(file)
    except json.JSONDecodeError:
        atickers ={}
        with open(json_file_path, "w") as file:
            json.dump({},file)
#dumps atickers to the data json
def _save_json():
    with open(json_file_path,"w") as file:
        json.dump(atickers,file)
#get data loads data from json to the atickers
def get_data(ticker:str)->np.array:
    _load_json()
    down = None
    if ticker not in atickers:
        down = _update_ticker_data(ticker)
        atickers[ticker] = date.today().isoformat()
        print(atickers)
        _save_json()

    else:
        print(f"last updated {atickers[ticker]} do you want to update {ticker} data? y-> Yes, n-> no")
        dec = input()
        dec = dec.lower()
        if dec =="y":
            down = _update_ticker_data(ticker)
            _save_json()
        else:
            filename = f"{ticker}.csv"
            filepath = os.path.join(csv_folder,filename)
            down = pd.read_csv(filepath)
    return down.to_numpy()

# returns the downloaded ticker data
# updates the aticker date
def _update_ticker_data(ticker):
        filename = f"{ticker}.csv"
        fullpath = os.path.join(csv_folder,filename)
        down = yf.download(ticker,progress=False,period="max")
        print(down.columns)
        down = down.reset_index()
        if isinstance(down.columns, pd.MultiIndex):
            down.columns = down.columns.get_level_values(0)

        down.to_csv(fullpath,index=False)
        atickers[ticker] = date.today().isoformat()
        return down
def get_close_data(t)->np.ndarray:
    arr = get_data(t)
    arr = np.transpose(arr)
    ret = arr[1]
    return ret