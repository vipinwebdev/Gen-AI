import numpy as np
import pandas as pd

np_array = np.array([1,2,3,4,5,6])
numbers = pd.Series(np_array)
print(f'\nSeries using numpy array:\n{numbers}')
