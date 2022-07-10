import numpy as np

# [0, 1) 난수 생성
a = np.random.random((2, 3))
print(type(a))
print(a)
b = a.reshape(3, 2)
print(b)

# 정규분포의 난수 생성
c = np.random.randn(3, 4)
print(c.reshape(2, 6))

# 값이 모두 1인 텐서
d = np.ones((4, 5))
print(d.reshape(2, 5, 2))

# 값이 모두 0인 텐서
e = np.zeros((3, 4))
print(e.reshape(2, 3, 2))
