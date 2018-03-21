[문제64] 입력값을 더하는 함수를 작성하세요.
x = 0
def add(num):
    global x
    x += num
    return x


print(add(2))
>>>2

print(add(8))
>>>10

################################################################
total = [0]
def add(arg):
    total[0] = arg
    return total[0]

print(add(8))

total   #위와 같은식으로 진행하면 함수 내에서도 글로벌로 처리가 된다.
################################################################


[문제65] 아래와 같이 변수에 값이 들어 있습니다. exchang함수에 x변수에 값을 넣으면 y로 변환하는 함수를 만드세요.

x = ["귀도","반","로섬"]
y = ["Guido","van", "Rossum"]

def exchange(x):
    for i in range(len(x)):
        x[i] = y[i]
        print(x)

exchange(x)
print(x)
print(y)


#변수 x에 영향없이 변화를 줄 때
import copy

def exchange(x):
    c = copy.deepcopy(x)
    for i in range(len(x)):
        c[i] = y[i]
        print(c)

exchange(x)
print(x)
print(y)


#x에다가 미리 x를 뒤집어 씌우면 메모리의 id자체가 변하게 된다.
#즉, 새로운 로컬x변수가 생기게 되는거고 함수안에서 사용되어도 밖에는 영향을 주지 않게된다.
def exchange(x):
    x = x[:]
    for i in range(len(x)):
        x[i] = y[i]
    print(x)
    
exchange(x)
print(x)
print(y)
   

[문제66]약수를 구하는 divisor 함수를 생성하세요.

1이상의 숫자를 입력하세요: 100
[100, 50, 25, 20, 10, 5, 4, 2, 1]

def divisor():
    x = []
    y = []
    num = int(input("1이상의 숫자를 입력하세요 : "))
    for i in range(1,num+1):
        if num%i == 0:
            x.append(i)
    for i in range(len(x)):
        y.append(x.pop())
    print(y)

divisor()

import time

def divisor():
    start = time.time()
    x = []
    num = int(input("1이상의 숫자를 입력하세요 : "))
    for i in range(1,num//2 +1):
        if num%i == 0:
            x.append(i)
    x.append(num)
    x.reverse()
    print(x)
    end = time.time() - start 
    return end

divisor()

num1 = int(input("1이상의 숫자를 입력하세요: "))
def divisor(num1):
    num2 = int(num1/2)  #홀수의 경우는 소수점이 발생할수도 있으므로int를 넣어준다.
    num3 = []
    num3.append(num1)
    while num2 >= 1:
        if num1 % num2 == 0:
            num3.append(num2)
        num2 -= 1
    return(sorted(num3))
    #return(sorted(num3,reverse = False))

print(divisor(num1))

재귀호출 = 자기자신을 다시 호출한다.
         = 반복문 + stack(스택)
         
def cn(n):
    if n <= 0:
        print("종료")
    else:
        print(n)
        cn(n-1)
        
cn(5)

#유클리드 호제법을 생각해보자.
def fac(num):
    if num == 1 or num == 0:
        return 1
    return fac(num-1) * num

fac(10)


def fac(num):
    if num == 0:
        print(1)
    elif num >= 1:
        x = 1
        for i in range(1,num+1):
            x = x * i
        print(x)
    else:
        print("잘못된 입력값입니다.")

fac(2)


최대 공약수
def dd(x,y):
    if y ==0:
        return x
    return dd(y,x%y)

dd(24,36)

1. 입력으로 두수 m,n(m>n)dl emfdjdhsek
2. n이 0이라면 m을 출력하고 알고리즘을 종료한다.
3. m이 n으로 나누어 떨어지면, n을 출력하고 알고리즘을 종료한다.
4. 그렇지 않으면 m을 n으로 나눈 나머지를 새롭게 m에 대입하고, m과 n을 바꾸고 3번으로 돌아간다.

[문제 68]stddev(2,3,1,7) 표준편차를 구하세요 stddev함수를 생성하세요

평균  = 관측값의 합 / 데이터 수
편차 = 관측값 - 평균
편차 제곱의 합 = (편차 **2) + (편차 **2)
분산  = 편차 제곱의 합 / 데이터의 수(자유도)
표준편차 = 분산에 루트

import math
math.sqrt(분산)
sum(인수)
len(인수)

math.sqrt(2)

## 내꺼 1
def stddev(*num):
    
    mean = sum(num) / len(num)
    
    v = []
    for i in num:
        v.append(i - mean)
    
    v2 = []
    for i in v:
        v2.append(i**2)
    
    return math.sqrt(sum(v2) / len(v2))
    
stddev(2,3,1,7)


## 내꺼 2
def stddev(*num):
    
    def mean(num):
        return sum(num) / len(num)
    
    def dev(num):
        v = []
        for i in num:
            v.append(i - mean(num))
        return v
    
    def var(num):
        v2 = []
        for i in dev(num):
            v2.append(i**2)
        return v2
    
    return math.sqrt(sum(var(num)) / (len(num)-1))


## 선생님꺼
def stddev(*arg):      # * 을 넣을 경우는 자료를 여러개 넣을 수 있지만 인자값에 리스트 형식의 데이터를 집어넣게 되면 오류가 난다.
    
    def mean():
        return sum(arg) / len(arg)
    
    def variance(m):
        total = 0
        for i in arg:
            total += (i-m) ** 2
        return total / (len(arg) - 1)
    v = variance(mean())
    return math.sqrt(v)

stddev(2,3,1,7)



## 디렉토리 주소 추가하는 법
## path 추가
import sys
sys.path
sys.path.append('C:\\Python')
sys.path

#모듈이름이 stddev.py로 되어있으므로 import
import stddev
round(stddev.stddev(2,3,1,7),6)

from stddev import *
round(stddev.stddev(2,3,1,7),6)

##sys.path에 C:\\Python을 매번 해주기 힘드므로 환경설정을 이렇게 해주면 된다.
컴퓨터 > 속성> 고급시스템설정 > 고급> 환경변수 > 새로만들기 > (변수이름 : PYTHONPATH, 변수값 : C:\Python)




def mean(*num):
    return sum(num) / len(num)
    
def dev(*num):
    v = []
    for i in num:
        v.append(i - mean(num))
    return v
    
def var(*num):
    v2 = []
    for i in dev(num):
        v2.append(i**2)
    return v2

import stddev
lst = [1,2,3,4,5]
stddev(lst)
