[문제132] emp.csv file에 있는 데이터 중에 100번 사원정보를 출력하세요.

import csv


file = open ("c:/r/emp.csv","r")
emp = csv.reader(file)
for i in emp:
    if i[0] == '100':
        print(i)

from pandas import Series,DataFrame
import pandas as pd

emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])
emp[emp['empid'] == 100]


oring = pd.read_csv("c:/r/c.csv")
oring



[문제133] emp.csv file에 있는 데이터 중에 직업이 ST_CLERK 인 사원들의 이름과 급여, 직업을 출력하세요

file = open ("c:/r/emp.csv","r")
emp = csv.reader(file)
for i in emp:
    if i[2] == 'ST_CLERK':
        print(i[1],i[5],i[2])

# pandas
emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])
emp[emp["job"] == "ST_CLERK"][["name","sal","job"]]

print(emp.loc[emp['job']=='ST_CLERK',['name','sal','job']])


[문제134] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요
emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])
emp[emp["sal"] >= 10000][["name","sal","hire_date"]]

file = open ("c:/r/emp.csv","r")
emp = csv.reader(file)
for i in emp:
    if float(i[5]) >= 10000:
        print(i[1],i[5],i[4])

[문제135] 급여 10000 이상인 사원들의 이름과 급여, 입사일를 출력하세요. 급여를 기준으로 내림차순하세요.

emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])
emp[emp["sal"] >= 10000][["name","sal","hire_date"]]

print(emp[['name','sal','hire_date']][emp['sal']>=10000].sort_values('sal',ascending = False))
print(emp.loc[emp['sal']>=10000,['name','sal','hire_date']].sort_values('sal',ascending = False))


file = open ("c:/r/emp.csv","r")
emp = csv.reader(file)
emp_list= []
for i in emp:
    if float(i[5]) >= 10000:
        emp_list.append(i)
        
emp_list_sorted = sorted(emp_list,reverse=True,key = lambda x: x[5])

for i in emp_list_sorted:
    print(i[1],i[5],i[4])
    
    
    
[문제136] 급여를 많이 받는 순으로 10위 까지를 구하세요. 

emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])
emp.sort_values('sal',ascending = False)[0:10]

[문제137] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업을 출력하세요.
emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])
emp[['name','sal','job']][emp['job'].isin(['AD_VP','AD_PRES'])]


[문제138] 직업이 AD_VP ,AD_PRES 아닌 사원들의 이름, 급여, 직업을 출력하세요.
emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])
emp[['name','sal','job']][~emp['job'].isin(['AD_VP','AD_PRES'])]

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA   #nan 이라는 애를 NA로 쓰겠다

obj = Series([1,2,3,None,5])
obj = Series([1,2,3,np.nan,5])
obj = Series([1,2,3,NA,5])

obj.fillna(0)

obj.isnull()
pd.isnull(obj)

obj.notnull()
pd.notnull(obj)

obj[obj.notnull()]
obj.dropna()

df = DataFrame([[1,2,3,],[1,NA,NA],[NA,NA,NA],[NA,2,3]])

df.dropna()  #Nan하나라도 있으며 ㄴ제외
df.dropna(how = 'all') #rowdp모든값이 Nan이면 제외

df[4] = NA

df.dropna(how = 'all',axis = 1) #컬럼에 모든 값이 Nan으로 되어있는 컬럼만 제외

df.fillna(0)
df[0].fillna(0)

df.fillna({0:0,1:1,2:2,4:4})
df.fillna(0,inplace = True)  #바로 수정한다.
df

df = DataFrame([[1,2,5],[NA,NA,4],[3,2,NA],[2,NA,3]])
df.fillna(method='ffill')
df.fillna(method='bfill')



[문제 139]커미션이 null 인 사원들의 이름과 커미션을 출력하세요 
emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])

emp[emp['comm'].isnull()][['name','comm']]

[문제140] 커미션이 null이 아닌 사원들의 이름과 커미션을 출력하세요.
emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])

emp[emp['comm'].notnull()][['name','comm']]



apply라는 메소드 공부
s1 = Series([1,2,3])

s1**2
def square(x):
    return x**2
square(2)

apply함수는 행, 열값을 인수값으로 받아서 반복하여 그 함수를 적용한다.

s1.apply(square)
s1.apply(lambda x: x**2)

df = DataFrame([[1,2,3],[4,5,6]])

df.apply(square,axis = 0)
#0 : 각 컬럼이 함수에 적용, 1: 각 row가 함수에 적용
df[0].apply(square)

import numpy as np

df.apply(np.sum, axis = 0)
df.apply(np.sum, axis = 1)

df.apply(lambda x: x**2)
df[0].apply(lambda x: x**2)

[문제141] 이름 첫글자가 S 로 시작하는 사원들의 이름을 출력하세요

emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])

def first_character(w):
    if w[0] == 'S':
        return True
    return False

print(emp[['name','sal']][emp['name'].apply(first_character)])    
print(emp.loc[emp['name'].apply(first_character),['name','sal']])
print(emp[['name','sal']][emp['name'].apply(lambda x: x[0]=='S')])    



