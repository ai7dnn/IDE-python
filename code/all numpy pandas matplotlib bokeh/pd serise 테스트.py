import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(1000, 4), columns=['A', 'B', 'C', 'D'],
                  index=pd.date_range('1/1/2020', periods=1000))
df = df.cumsum()
print(df.head())

df.plot()
plt.show()