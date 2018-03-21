[문제167] 부서이름별 총액 급여를 출력하세요.  

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:/r/dept.csv", names = ['deptno','deptname','mgr','locno'])

a = pd.merge(emp[['deptno','sal']],dept[['deptno','deptname']],on = 'deptno')
a = a['sal'].groupby(a['deptname']).sum()  #여기서 끝내면 인덱스는 부서이름이 된다.
a

a = DataFrame(a)
a = a.reindex([10,20,30,40,50,60,70,80,90,100,110])  #인덱스 번호때문에 merge가 안될수도 있다.
pd.merge(dept[['deptno','deptname']],a,left_on = 'deptno',right_index = True)

emp['sal'].groupby([emp['deptno'],emp['job']]).sum()

empgroup = emp.groupby(['deptno','job'])

empsal = empgroup['sal']

empsal.agg('sum')
empsal.agg(['sum','mean','count','max','min'])


lst = [10,20,30,40,50]

lst * 2     #반복이 된다.

def f1(x):
    return x *2
f1(lst)

def f2(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x
f2(lst)

(lambda x: x*2)(lst)    #안된다!

map(lambda x: x*2, lst)     #map객체가 만들어진다.
list(map(lambda x: x*2, lst))   #앞에list를 덧씌워준다.

def f1(x):
    return x *2
list(map(f1,lst))

map(함수, 반복해야할 자료형) 은 함수와 반복가능한 자료형을 입력받아서
 입력받은 자료형의 각 요소가 함수에 의해 수행된 결과를 묶어서 리턴하는 함수
 
 
[문제168] x변수에는 1,2,3,4,5  y변수에는 6,7,8,9,10 들어 있다. f(x,y) = x2 + y 를 구하세요.(lambda, map 함수를 이용하세요)

x = [1,2,3,4,5]
y = [6,7,8,9,10]

list(map(lambda x,y: 2*x + y, x,y))

from pandas import Series, DataFrame
import pandas as pd

x= pd.Series([1,2,3],index = ['one','two','three'])

y = pd.Series(['하나','둘','셋'],index = [1,2,3])
x
y
x.map(y)

[문제169] emp.csv는 pandas로 읽고  dept.csv는 일반 csv로 읽어 들인 후 조인을 수행하세요.

##emp 읽어오고!!
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

##dept 읽어오고!!
import csv
file = open("c:/r/dept.csv",'r')
dept_csv= csv.reader(file)
dept={}
for i in dept_csv:
    if i[0] != dept:
        dept[int(i[0])] = i[1]

#확인하고
for k,v in dept.items():
    print(k,v)

#합쳐라
emp['deptname'] = emp['deptno'].map(dept)
print(emp[['empid','deptno','deptname']])


[문제170] happiness 변수에 문장이 있습니다. 행복이란 단어가 몇개 나오는지 분석하시고, 위치정보도 출력해주세요.

happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다”라고 규정하고 있다. 행복추구권은 근대 입헌민주주의의 핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나, 최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'

a = 0
print('단어의 갯수 : ',happiness.count("행복"))
for i in  range(happiness.count("행복")):
    a = happiness.find("행복",a+1)
    print('단어의 위치 : ',a)
    
    
a = 0
while happiness.find('행복',a) != -1:
    a = happiness.find("행복",a)
    print("단어의 위치 : " , a)
    a += 1



파일 입출력

        파일 생성
        파일 객체 = open(파일이름,파일열기모드)
        파일 모드
            r : 읽기(파일 읽기)
            w : 쓰기(기존의 파일이 있을경우는 파일안에 내용이 전부지워지고 열린다,
                     파일이 없는 경우는 새로운 파일이 생성된다.)
            a : 추가

file = open("c:/python/test.txt",'w')
file.write("행복하자")
file.close()


file = open("c:/python/test.txt","w")

for i in range(1,11):
    content = " %d 번째줄 ..... \n"%i
    file.write(content)

file.close()

import os
os.path.exists("c:/python/test.txt")  #파일의 존재여부를 확인

file = open("c:/python/test.txt","w")

for i in range(1,11):
    content = "{} 번째줄 ..... \n".format(i)
    file.write(content)

file.close()

파일 읽기
file = open("c:/python/test.txt","r")
data = file.readline() #첫번째 라인만 읽고 끝난다.
print(data)
file.close()

##한줄씩 읽기
file = open("c:/python/test.txt","r")
while True:
    data = file.readline()
    if not data:
        break
    print(data,end='')
file.close()

#조금 이상하게 나온다!!!!
file = open("c:/python/test.txt","r")
data = file.readlines() #모든 라인을 읽어서 리스트에 저장
print(data)
file.close()

#프린트와 프린트사이에 공백이 없도록 하기위해서!
file = open("c:/python/test.txt","r")
data = file.readlines() #모든 라인을 읽어서 리스트에 저장
for i in data:
    print(i,end = '')
file.close()

#한꺼번에 쭈욱 읽어줌
file = open("c:/python/test.txt","r")
data = file.read() 
print(data)
file.close()

with open("c:/python/test.txt","w") as file:
    file.write("복습하자")

with open("c:/python/test.txt","r") as file:
    line = file.readlines()
    for i in line:
        print(i,end = '')
        
lines = ['안녕하세요','제임스딘 입니다.']

with open("c:/python/test.txt","w") as file:
    for i in lines:
        file.write(i) #줄바꿈이 없어서 한줄에 연결된다.

with open("c:/python/test.txt","w") as file:
    for i in lines:
        file.write(i+'\n') #줄바꿈 해결


[문제171] happiness 변수에 단어의 수를 구하세요.

happiness = '우리나라 「헌법」 제10조는 “모든 국민은 인간으로서의 존엄과 가치를 가지며, 행복을 추구할 권리를 가진다”라고 규정하고 있다.행복추구권은 근대 입헌민주주의의 핵심인 개인주의·자유주의를 그 사상적 기반으로 하고 있다. 행복추구권에 있어서 행복은 다의적인 개념으로, 각자의 생활조건이나 가치관에 따라 다르게 이해될 수 있으나, 최소한 인간적인 고통이 없는 상태 내지 만족감을 느낄 수 있는 행복한 상태를 의미한다.'
a = happiness.split()
print(a)
print('단어수 : [%d]'%len(a))


##똑같은 컬럼의 파일을 동시에 여는 방법!
c:/python/emp1.csv
c:/python/emp2.csv

import os
import glob
import pandas as pd
from pandas import Series,DataFrame

file = "c:/python/emp*.csv"
file_list = glob.glob(file)
print(file_list)
emp = pd.DataFrame()
for i in file_list:
    temp = pd.read_csv(i,names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
    emp = emp.append(temp)
emp
