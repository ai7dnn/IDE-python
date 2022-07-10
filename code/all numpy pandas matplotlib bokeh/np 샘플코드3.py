# http://riseshia.github.io/2017/01/30/numpy-tutorial-with-code.html

import numpy as np

a = np.arange(12) # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
print(a)

b = a.reshape(4, 3) # 변환된 행렬을 반환
print(b)
a.resize((3, 4)) # 자체를 변환함
print(a)

b = a.flatten()
print(b)
b = a.ravel()
print(b)

b = a.T # 전치 행렬
print(a)
print(b)

a.shape = 2, 6 # 파괴적
print(a)

b = a.reshape(3, -1) # 변환된 행렬을 반환
print(b)
