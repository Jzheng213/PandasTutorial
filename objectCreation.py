import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creating a Series by passing  list of values, letting pandas create a default integer index:
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

