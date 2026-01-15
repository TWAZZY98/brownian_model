import pandas as pd
import csvdatabase as csvd
import stochasticprocess as sp
import testfile
from matplotlib import pyplot as mp
import numpy as np

def main():
    #g = sp.geometricbrownian(304,0.30,0.1,1,100,5)
    #g.simplepath()
    #g.multiplesimplepath(100)
    
    data = csvd.get_close_data("NVDA")
    n = sp.geometricbrownian(data[len(data)-1],0.01,0.005,2,200,42)
    g = n.multiplesimplepath(10000)
    data_x = len(data[6500:])
    new_time_grid = n.get_time_grid()
    for i in range(len(n.get_time_grid())):
        new_time_grid[i-1] = new_time_grid[i-1]*100 + data_x-1
    mp.plot(new_time_grid,g)
    mp.plot(data[6500:])
    mp.show()
    

if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()