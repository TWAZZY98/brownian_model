import numpy as np
from matplotlib import pyplot as mp


def bar_model_data(data:np.array)->None:
    mp.hist(data)
    mp.show()
    