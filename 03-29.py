numpy : numerical python

    - 고성능 과학 계산 컴퓨팅과 데이터 분석에 필요한 기본 패키지
    - 계산 속도가 빠르고 메모리를 효율적으로 사용
    - 벡터 산술연산, 브로드캐스팅 기능을 사용하여 다차원 배열을 제공
    - 반복문을 사용할 필요 없이 전체 데이터 배열에 대해서 빠른 연산 제공
    
import numpy as np

# 다차원 배열 객체 : ndarray
data = np.random.randn(2,3)
data
type(data)

data.shape
data.dtype
data.ndim

data * 2
data - data
data + data
data / data
data * data

data = [1,2,3,4,5,6]
n = np.array(data)
n
n.shape
n.ndim
n.dtype


data2 = [[1,2,3],[4,5,6]]
n2 = np.array(data2)
n2
n2.shape
n2.ndim
n2.dtype

np.ones(5)
np.ones((3,3))

#영행렬
np.zeros(5)
np.zeros((3,3))
np.zeros((3,2,5))

#단위 행렬
np.eye(3)
np.eye(5)


np.arange(10)
np.arange(10,20)


data1 = np.array([[1,2,3],[4,5,6]])
type(data1)
data1.shape
data1.dtype

data2 = np.array([[10,20,30],[40,50,60]])

data1 + data2
data1 - data2
data1 * data2
data2 / data1
data2 / 5
data1 **2

data1 = np.arange(10)
data1
data1[1]
data1[0:5]
data1[5] = 50
data1[5:]
data1[:5]


data2 = np.array([[1,2,3],[4,5,6]])
data2[0]
data2[1]
data2[1][2]
data2[1,2]
data2[1,:2]
data2[1:,:2]
data2[:,1]
data2[:,1:]

#배열의 축바꾸기
data = np.arange(6).reshape(2,3)
data
#전치행렬
data.T

#행렬의 곱
np.dot(data.t,data)

data1 = np.arange(24).reshape(2,3,4)

#행과 열을 바꾼다 2x3 -> 3x2
data1.transpose(0,1,2)
data1.transpose(0,2,1)
data1.swapaxes(1,2)

data = np.arange(5)

#제곱근
np.sqrt(data)

#제곱
data **2
np.square(data)

data1 = np.arange(0,20,2)
data2 = np.arange(0,30,3)

np.add(data1,data2)

#각 배열의 원소 중에 작은값
np.minimum(data1,data2)

np.maximum(data1,data2)

name = np.array(['홍길동','박찬호','손흥민','윤건','홍길동','윤건','나얼','김건모'])

name
type(name)
name.ndim

name == '홍길동'

data = np.arange(24).reshape(8,3)
type(data)
data.dtype
data.ndim

data[name == '홍길동']

data[name != '홍길동']

condistion = (name == '나얼')|(name == '윤건')
data[condistion]

data[data > 10]
data[name == '홍길동'] = 0


arr = np.arange(10)

arr
arr.shape
arr.reshape((5,2),order = 'C') # 행 우선
arr.reshape((5,2),order = 'F') # 열 우선

arr = np.arange(10).reshape((5,2))
arr.ravel('F')
arr.ravel('C')

arr.flatten()


arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

np.concatenate([arr1,arr2],axis = 0)
np.concatenate([arr1,arr2],axis = 1)

np.vstack((arr1,arr2))
np.hstack((arr1,arr2))

arr = np.arange(3)
arr
arr.repeat(2)
arr.repeat([2,3,4])


arr = np.random.randn(2,2)
arr

arr.repeat(2,axis=0)
arr.repeat(2,axis=1)
arr.repeat([2,3],axis=1)

np.tile(arr,2)
a = np.array([[1,2],[3,4]])
a

np.sum(a)
np.sum(a,axis = 0)
np.sum(a,axis = 1)

np.mean(a)
np.mean(a,axis = 0)
np.mean(a,axis = 1)

np.var(a)
np.std(a)

np.cumsum(a)
np.cumsum(a,axis = 0)
np.cumsum(a,axis = 1)

np.prod(a)
np.prod(a,axis = 0)
np.prod(a,axis = 1)

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
y = np.array([1,0,1])
z = np.empty_like(x) #x와 동일한 shape를 가진 행렬을 생성
z = np.zeros((4,3))

z = x + y

for i in range(4):
    z[i,:] = x[i,:] + y
z




x + np.tile(y,4).reshape(4,3)

x = np.array([3,3,3,2,2,1,1,4,4,4,5,5,5,5,1,8,1,8])
np.unique(x)
sorted(set(x))

x = np.array([1,2,3,4,5,6,2,4,4])
np.in1d(x,[2,3,4])
np.intersect1d([1,3,4,3],[3,1,2,1])
np.setdiff1d([1,3,4,3],[3,1,2,1])

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[2,3,5],[7,8,6]])

np.setdiff1d(x,y)
np.intersect1d(x,y)
np.union1d(x,y)


x = np.array([5,2,4,3,1])
sorted(x)
sorted(x,reverse = True)

ix = x.argsort()
ix

x[ix]

x = np.random.randn(3,4)
x
x[:,x[0].argsort()]
