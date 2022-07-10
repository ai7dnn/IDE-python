import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Series는 1차원 데이터를 다루는 데 효과적인 자료구조
# value와 index의 형태를 지니는 Pandas의 자료 구조
# 별도의 인덱스 레이블을 지정하지 않으면 자동적으로
# 0부터 시작되는 디폴트 정수 인덱스를 사용
# 다음은 인덱스를 날짜 1000개로 지정, 자료 값은 난수 1000개
# 즉 2020년 1월 1일부터 1000일까지 정규분포 1000개를 지정
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2020', periods=1000))

print(ts, '\n')

# 위 자료에서 컬럼 값을 계속 더하여 저장
ts = ts.cumsum()
print(ts)

# 그리기
ts.plot()
plt.show()