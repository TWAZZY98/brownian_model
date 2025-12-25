import math
import numpy
import pandas

    #_mean:(float)#=sum(element)/n
    #_sd:(float)#=sqrt(sum(mean-element)/(n-1))
    #zscore=(observed-sample mean)/sd
    
    #add conditioins for when set is null
    
def calc_mean(set)->float|None:
    if set.empty:
        return None
    return float(set.illoc[:,0].mean())
    
def calc_sd(set)->float|None:
    if set.empty:
        return None
    return float(set.iloc[:,0].std(ddof=1))