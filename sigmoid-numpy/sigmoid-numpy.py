import numpy as np

def sigmoid(x):
    res = np.array(x, dtype = float)

    return 1 / (1 + np.exp(-res))