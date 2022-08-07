import numpy as np

def get_chess(a):
    arr = np.zeros((a, a))
    arr[1:,0::2][::2] = 1
    arr[:,1::2][::2] = 1
    return arr

print(get_chess(8))
