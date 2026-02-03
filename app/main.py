import pandas as pd
import csvdatabase as csvd
import stochasticprocess as sp
import normalmodel as nm

from matplotlib import pyplot as mp
import numpy as np

def main():
    #g = sp.geometricbrownian(304,0.30,0.1,1,100,5)
    #g.simplepath()
    #g.multiplesimplepath(100)
    
    nm.bar_model_data(sp.predict_for_data('AAPL',100,100,0,0,10))
    # n= sp.geometricbrownian(100,0.1,0.4,40,40)
    # n.multiplesimplepath(100)
if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()



