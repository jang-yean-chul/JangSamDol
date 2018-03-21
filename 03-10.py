[문제106] 부서별 급여의 총액을 구하세요. 아래 결과 처럼 출력하세요.

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 31584.6
70 10000.0
80 304500.0
90 82655.1
100 51608.0
110 20308.0
non 7000.0



file = open ("c:/r/emp3.csv","r")
emp = csv.reader(file)
data = []
for i in emp:
    data.append(i)

for i in range(len(data)):
    if data[i][10] == '':
        data[i][10] = '9999'

file = open ("c:/r/emp3.csv","r")
emp = csv.reader(file)
ddd= []
for i in emp:
    ddd.append(i[10])
depart = list(set(ddd))

for i in range(len(depart)):
    if depart[i] == '':
        depart[i] = '9999'
    depart[i] = int(depart[i])
depart.sort()


for i in depart:
    tosal = 0
    for j in data:
        if int(j[10]) == i:
            tosal += float(j[7])
    print(i, tosal)


###선생님
def get_key(key):
    if key == '':
        return int(1000)
    else:
        return int(key)
    
for k,v in sorted(dept_sum.items(),key = lambda k:get_key(k[0])):
    if k == '':
        print('non',v)
    else:
        print(k,v)
        
        
        
[문제107] lst 변수에 2,6,1,8,7,9 가 입력 되어 있습니다. 
lst변수를 입력하면 최대값을 리턴 해주는 maxF함수를 생성하세요.

lst = [2,6,1,8,7,9]

def maxF(arg):
    v_max = 0
    for i in arg:
        if i>v_max:
            v_max = i
    return v_max

print(maxF(lst))
print(max(lst))


[문제108] lst 변수에 2,6,1,8,7,9 가 입력 되어 있습니다. 
lst변수를 입력하면 최소값을 리턴 해주는  minF함수를 생성하세요.

lst = [2,6,1,8,7,9]

def minF(arg):
    v_min =arg[0]
    for i in arg:
        if i<v_min:
            v_min = i
    return v_min

print(minF(lst))
print(min(lst))

[문제109] 단어, 알파벳을 입력값으로 넣어서 단어 안에 알파벳 수를 출력하세요

<화면예>

wordF('happy','p')
2

def wordF(arg,arg2):
    a = arg
    return a.count(arg2)

def wordF(arg1,arg2):
    cn = 0
    for i in arg1:
        if i == arg2:
            cn += 1
    print(cn)


[문제110] 단어를 입력값으로 넣어서 알파벳을 출력하는데 중복되는 알파벳은 하나만 출력하세요.

alphaF('happy')
['h', 'a', 'p', 'y']

alphaF('intelligence')
['i', 'n', 't', 'e', 'l', 'g', 'c']

def alphaF(arg):
    a = []
    for i in arg:
        if i not in a:
            a.append(i)
    print(a)


[문제111] 단어 철자의 빈도수를 출력하세요.


alphaF('intelligence')
{'i': 2, 'n': 2, 't': 1, 'e': 3, 'l': 2, 'g': 1, 'c': 1}

alphaF('happy')
{'h': 1, 'a': 1, 'p': 2, 'y': 1}


def alphaF(arg):
    a = {}
    for i in arg:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    print(a)
    
    
    
■   pandas
    - 데이터 분석 기능을 제공하는 라이브러리
    - 1차원 배열 : Series
    - 2차원 배열 : DataFrame
import pandas as pd
from pandas import Series,DataFrame
# Series
    - 1차원 배열
    - index(색인) 배열의 데이터에 연관된 이름을 가지고있다.
s = Series([10,20,30,40])
s
s.index
s.values
s.index=['a','b','c','d']
s

s2 = Series([10,20,30,40],index=['a','b','c','d'])
s2.index
s2.values

s2['a']
s2[['a','b']]
s2[0]
s2[0:3]
s2[s2>20]

'a' in s2

dict = {'a':10,'b':20,'c':30,'d':40}
s3 = Series(dict)
s3

s4 = {'a','b','c','d'}
s5 = Series(dict, index = s4)
s5


s4 = {'a','b','c','z'}
s5 = Series(dict, index = s4)


# DataFrame
    - 2차원 배열
    - 표 같은 스프레드시틔 형식의 자료구조
    - 각 컬럼은 서로다른 종류으 값(숫자, 문자, 불리언)
    - R의 언어는 data.frame
    
df1 = DataFrame([[1,2,3],[4,5,6,],[7,8,9]])
df1

data = {'도시':['서울','광주','부산','인천'],'인구수':[20000,1000,1500,500]}
df2 = DataFrame(data)
df2


df2 = DataFrame({'도시':['서울','광주','부산','인천'],'인구수':[20000,1000,1400,500]})
df3 = DataFrame(data,columns = ['인구수','도시'],index = ['one','two','three','four'])
df3
df3.도시
df3['도시']
df3['인구수'] *10 

df3.index
df3.columns

df3.ix['one']
df3.ix[0]

v = Series([1000,2000,3000,4000],index = ['one','two','three','four'])
v
df3['부채'] = v
df3



#행 삭제
obj  = Series(np.arange)

obj = obj.drop('e')
obj = obj.drop(['c','d'])

df = DataFrame(np.arange(16).reshape(4,4), index = ['w','x','y','z'], columns = ['one','two','three','four'])
df

df2 = df.drop(['x','z'],axis = 0) # axis = 0 행

df2 = df.drop(['four'],axis = 1) # axis = 1 열

df2 = df.drop(['one','four'],axis = 1) # axis = 1 열

####

obj = Series([10,20,30,40], index = ['a','b','c','d'])

obj['a']
obj[0]

obj[1:3]
obj['b':'c']

obj[['a','c']]
obj[[0,2]]

obj[obj<30]

#행렬 만들 때 처리속도를 높여주는 것
import numpy as np
df = DataFrame(np.arange(16).reshape(4,4), index = ['w','x','y','z'], columns = ['one','two','three','four'])
df

df['one'] #dataframe에서는 []안에 열이름을 적는다 
df[['one','two']]
df[2:]
df[0:2]

df < 5
df[df < 5]
df[df['one'] < 5]
df[df < 5] = 0
df

df.loc['x'] #index의 이름으로 접근
df.iloc[0] #index의 행의 번호를 기준으로 접근
df.ix['x','one']
df.loc['x','one']
df.ix[0,'one']

