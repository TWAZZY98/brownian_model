import pandas as pd
import csvdatabase as csvd
import stochasticprocess as sp

from matplotlib import pyplot as mp
import numpy as np

def main():
    #g = sp.geometricbrownian(304,0.30,0.1,1,100,5)
    #g.simplepath()
    #g.multiplesimplepath(100)
    
    sp.predict_for_data('NVDA',30,30,0.015,0.025,100)
    

if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()



