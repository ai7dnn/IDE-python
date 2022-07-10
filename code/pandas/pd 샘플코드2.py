import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200102', periods=6))
print(s)

s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s)
s.str.lower()
print(s)

df = pd.DataFrame(np.random.randn(10, 4))
print(df)

