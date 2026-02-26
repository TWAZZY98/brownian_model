import numpy as np
from matplotlib import pyplot as mp


def bar_model_data(data:np.array)->float:
    m = np.mean(data)
    print(m)
    mp.hist(data)
    mp.show()
    return m
    