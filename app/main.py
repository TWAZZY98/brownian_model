import pandas as pd
import csvdatabase as csvd
import stochasticprocess as sp
import testfile

def main():
    g = sp.geometricbrownian(304,0.30,0.1,1,100,5)
    #g.simplepath()
    g.multiplesimplepath(100)
    
    

if __name__ == "__main__": 
    print(f"{__name__} is being run directly")
else: 
    print(f"{__name__} is being imported")
    
main()