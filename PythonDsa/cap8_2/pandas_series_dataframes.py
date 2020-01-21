# Time series com Dataframes
import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import style
import os

# Trabalhando com series de datas
print('Time series')
rng = pd.date_range('1/1/2018', periods=50, freq='H')
print(rng)
print('')

ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print('')

# Ploting
print('Plotando time-series pandas')
ts = pd.Series(np.random.randn(500), index=pd.date_range('01/01/2018', periods=500))
print(ts.cumsum())
ts.plot()
print('')

# DataFrame plot
# df_plot = pd.DataFrame(np.random.randn(500, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
# df = df_plot.cumsum()
# plt.figure(); df.plot(); plt.legend(loc='best')

