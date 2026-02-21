import pandas as pd
import csvdatabase as csvd
import stochasticprocess as sp
import normalmodel as nm

from matplotlib import pyplot as mp
import numpy as np
import GUI

def main():
    #g = sp.geometricbrownian(304,0.30,0.1,1,100,5)
    #g.simplepath()
    #g.multiplesimplepath(100)
    numOfSim = 1000
    days = 100
    d =sp.predict_for_data('AAPL',days,days,0,0,numOfSim)
    mean = nm.bar_model_data(d[0])
    vol_and_ret = d[1]
    GUI.brownian_sim_results(mean,numOfSim,vol_and_ret[1],vol_and_ret[0])
    # n= sp.geometricbrownian(100,0.1,0.4,40,40)
    # n.multiplesimplepath(100)

if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()



