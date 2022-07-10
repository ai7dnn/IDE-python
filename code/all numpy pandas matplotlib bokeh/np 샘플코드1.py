import numpy as np

# Return random floats in the half-open interval [0.0, 1.0).
# Alias for `random_sample` to ease forward-porting to the new random API.
a = np.random.random((2, 3))
print(a)
a = np.random.random_sample([2, 4])
print(a)

# 정규분포의 난수 생성
b = np.random.randn(2)
print(b)
b = np.random.randn(2, 3)
print(b)
b = np.random.randn(3, 4)
print(b)

# 값이 모두 1인 텐서
c = np.ones(3)
print(c)

# 값이 모두 0인 텐서
c = np.zeros((2, 3))
print(c)
c = np.zeros([3, 4])
print(c)
