# Hello World출력
import matplotlib.pyplot as mpt
import numpy as np
print('Hello World!!!')


# sin, cos 그래프 그리기
# %matplotlib inline

# import numpy as np
# import matplotlib.pyplot as mpt

# a=np.linspace(-np.pi, np.pi)

# mpt.plot(a, np.sin(a))
# mpt.plot(a, np.cos(a))
# mpt.show()


# 내장 데이터형
# built-in data type
a = 10
b = 10.1
c = "Python"
d = False
e = [10, 20, 30]
print(a, b, c, d, e)


# 변수형 출력
a = 10
print(type(a))


# 산술연산자
%matplotlib inline


a = 10
b = 20

s1 = a/b
s2 = a//b
s3 = a % b
s4 = a**b

print(s1, s2, s3, s4)


# 관계연산자
a = 10
b = 20

s1 = a < b
s2 = a > b
s3 = a <= b
s4 = a >= b
s5 = a == b
s6 = a != b

print(s1, s2, s3, s4, s5, s6)


# 논리연산자
%matplotlib inline


a = True
b = False
list = [10, 20, 30, 40, 50]

s1 = 25 in list
s2 = a and b
s3 = a or b
s4 = not a

print(s1, s2, s3, s4)


# 리스트
%matplotlib inline


list = ['apple', 10, "orange", 20]
list

type(list)

list.append(30)
list

list.insert(0, 1)
list

list.extend(["banana", "apple"])
list

list += [40]
list

list.index('apple')
list.index('apple', 1)
list
list.count("apple")
list
list.pop()
list
list.pop(1)
list


# 세트
%matplotlib inline


a = {10, 20, 30}
b = {30, 40, 50}

a.union(b)
a | b
a.intersection(b)
a & b
a-b


# 튜플
%matplotlib inline


a = (10, 20, 30, 40)

b = a[1]
print(b)


# 딕셔너리
%matplotlib inline


d = {'a': 10, 'b': 20, 'c': 30}

print(d['a’])

d['a'] = 11

d


# if
%matplotlib inline


score = 30

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')


# while
%matplotlib inline


a = 0

while a < 3:
    print(a)
    a += 1


# for
%matplotlib inline


for a in [10, 20, 30]:
    print(a)

for a in range(3):
    print(a)

list = [10, 20, 30]
itr = iter(list)

for a in itr:
    print(a)


# 컴프리핸션
a = [10, 20, 30]
b = [c+1 for c in a]
print(b)


a = [10, 20, 30]
c = [c*2 for c in a if c < 25]
print(c)


# 함수
%matplotlib inline


def addSum(a, b):
    rst = a+b
    return rst


print(addSum(10, 20))


%matplotlib inline


def addSum(a, b, c):
    rst = a+b+c
    return rst


lst = [10, 20, 30]
print(addSum(*t))


# 클래스
class Test:
    def __init__(self, a):
        self.a = a

    def addSum(self, b):
        print(self.a+b)


rv = Test(10)
rv.addSum(20)


%matplotlib inline


class Test:
    def __init__(self, a):
        self.a = a

    def addSum(self, b):
        print(self.a+b)


class SubTest(Test):
    def sqr(self, c):
        print(c*c)


rv = SubTest(10)
rv.sqr(10)
rv.addSum(20)


# 배열
%matplotlib inline


a = np.array([10, 20, 30, 40, 50])
print(a)

b = np.array([[10, 20, 30], [40, 50, 60]])
print(b)


print(np.zeros(10))  # 모든 값이 0인 배열
print(np.ones(10))  # 모든 값이 1인 배열
print(np.random.rand(10))  # 난수로 생성되는 배열
print(np.zeros((2, 3)))  # 모든 값이 0인 2차원배열
print(np.ones((2, 3)))  # 모든 값이 1인 2차원배열


print(np.arange(0, 1, 0.1))  # 0~1 사이 0.1 간격 배열
print(np.arange(10))  # 0 부터 간격 1씩 방10개
print(np.linspace(0, 1, 11))  # 0~1 사이 0.1 간격 방11개
print(np.linspace(0, 1))  # 0~1 사이 0.1 간격 방50개


arr1 = np.array([10, 20, 30, 40, 50, 60, 70, 80])
arr2 = arr1.reshape(2, 4)  # 2행4열 2차원 배열로 변환
arr3 = np.reshape(arr1, (2, 4))  # 2행4열 2차원 배열로 변환
print(arr2)
print(arr3)

arr4 = arr2.reshape(2, 2, 2)  # 2면2행2열 3차원 배열로 변환
print(arr4)

arr5 = arr4.reshape(4, 2)  # 4행2열 2차원 배열로 변환
print(arr5)

arr6 = arr5.reshape(-1)  # 1차원 배열로 변환
print(arr6)

arr7 = arr6.reshape(2, -1)  # 전체 배열을 2행으로 나누고 열은 자동계산
print(arr7)


# 브로드캐스트

arr1 = np.array([10, 20, 30, 40]).reshape(2, 2)
arr2 = np.array([1, 2])
arr3 = np.array([[1],
                 [2]])

print(arr1 + arr2)
print(arr1 + arr3)


# 배열함수

arr1 = np.array([[10, 20],
                [30, 40]])

print(np.sum(arr1))
print(np.sum(arr1, axis=0))
print(np.sum(arr1, axis=1))
print(np.max(arr1))
print(np.argmax(arr1, axis=0))
print(np.where(arr1 < 20, 5, arr1))


# matplotlib
# sin 그래프
%matplotlib inline  # 반드시 적어주는 코드


x = np.linspace(0, 2*np.pi)  # 0~2pi 까지
y = np.sin(x)

mpt.plot(x, y)
mpt.show()


# 축 이름, 그래프 제목, 범례

%matplotlib inline


x = np.linspace(0, 2*np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)

mpt.xlabel("x")
mpt.ylabel("y")

mpt.title("sin & cos graph")

mpt.plot(x, y_sin, label="sin")
mpt.plot(x, y_cos, label="cos", linestyle="dashed")
mpt.legend()

mpt.show()


# 산포도
%matplotlib inline


x_1 = np.random.rand(100)
y_1 = np.random.rand(100)
x_2 = np.random.rand(100)
y_2 = np.random.rand(100)

mpt.scatter(x_1, y_1, marker="+")
mpt.scatter(x_2, y_2, marker="x")

mpt.show()


# 이미지
%matplotlib inline


img = np.array([[1, 2, 3, 4, ],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

mpt.imshow(img, 'gray')
mpt.colorbar()

mpt.show()
