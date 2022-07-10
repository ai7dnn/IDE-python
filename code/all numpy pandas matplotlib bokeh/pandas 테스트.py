import numpy as np
import pandas as pd

dates = pd.date_range('20210101', periods=6)
print(dates)

# 정규분포에서 6행 4열의 난수 생성
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

print(df)
print(df.head()) # 첫 5개 행
print(df.tail(3)) # 마지막 3개 행
print(df.describe()) # 전체 통계 데이터

# 추가
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.T)
# print(df.sort_index(axis=1, ascending=False))
# print(df.sort_values(by='B'))
# print(df['A'])
# print(df[0:3])
# print(df.loc[dates[0]])
# print(df.iloc[3:5, 0:2])
# print(df[df.A > 0])
# print(df.mean())
# print(df.apply(np.cumsum))
