from dataclasses import replace
import numpy as np

def get_loto(num):
    number = np.arange(1,101)
    loto = np.random.choice(number, size=(num, 5, 5), replace=False)
    return loto

print(get_loto(4))

simplelist = [19, 242, 14, 152, 142, 1000]
print(np.mean(simplelist))