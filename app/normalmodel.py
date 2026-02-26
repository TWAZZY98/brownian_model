import numpy as np
from matplotlib import pyplot as mp


def bar_model_data(data:np.array)->float|None:
    if data is None:
        print("data to graph is none")
        return
    m = np.mean(data)
    mp.hist(data)
    mp.show()
    return m
    