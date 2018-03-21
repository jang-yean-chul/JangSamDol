[문제142] 이름이 g 로 끝나는 사원들의 이름, 급여 출력하세요
import csv
from pandas import Series,DataFrame
import pandas as pd

emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])

##1
for i in range(len(emp)-1):
    if emp["name"][i][-1] == "g":
        print(emp["name"][i],emp["sal"][i])

##2
emp[['name','sal']][emp['name'].apply(lambda x: x[-1] == 'g')]

##3
def last_letter(x):
    if x[-1] == 'g':
        return True
    return False

print(emp.loc[emp['name'].apply(last_letter),['name','sal']])


[문제143] 110번 사원의 급여보다 많이 받는 사원의 이름, 급여 출력하세요.
from pandas import Series,DataFrame
import pandas as pd

emp = pd.read_csv("c:/r/emp.csv",names = ["empid","name","job","mgr","hire_date","sal","comm","deptno"])

emp[['name','sal']][emp['sal']> int(emp['sal'][emp['empid']==110])]

emp[['name','sal']][emp['sal'].apply(lambda x: x > int(emp['sal'][emp['empid']==110]))]

for i in range(len(emp)-1):
    if emp['sal'][i] > int(emp['sal'][emp['empid']==110]):
        print(emp[['name','sal']][i])

emp[['name','sal']][emp['sal'] > emp['sal'][emp['empid']==110]]


##선생님
import  pandas  as  pd
emp = pd.read_csv("c:\data\emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
v_sal = emp[['sal']] [emp['empid'] == 110].values[0]
print(emp[['name','sal']][emp['sal'] > v_sal[0]])



import  csv

file = open("c:\data\emp.csv",'r')
emp_csv = csv.reader(file)
v_sal = []
for emp_list in emp_csv:
    if  emp_list[0] == '110':
        v_sal.append(emp_list[5])

file = open("c:\data\emp.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if float(emp_list[5]) > float(v_sal[0]):
        print(emp_list[1], emp_list[5])
     

[문제144]관리자 사원의 이름, 입사일, 급여 출력하세요.


import  pandas  as  pd
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
print(emp[['name','hire_date','sal']][emp['empid'].isin (emp['mgr'])])

import  csv

file = open ("c:/r/emp.csv","r")
emp = csv.reader(file)
v_mgr = []
for i in emp:
    for j in v_mgr:
        j = emp[3]
        if emp[0] == j:
            print(emp[1],emp[4],emp[5])




for emp_list in emp_csv:
    if (not emp_list[3] in v_mgr) & (emp_list[3] != ''):
        v_mgr.append(emp_list[3])
print(len(v_mgr))

file = open("c:/r/emp.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    for mgr in v_mgr:
        if emp_list[0] == mgr:
            print(emp_list[1],  emp_list[4], emp_list[5])


[문제145]101번 사원의 관리자 이름, 입사일, 급여정보를 출력하세요.

import  pandas  as  pd
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
mgr = emp[['mgr']][emp['empid']==101].values[0]
print(emp[['name','hire_date','sal']][emp['empid']==mgr[0]])



import  csv

file = open("c:/r/emp.csv",'r')
emp_csv = csv.reader(file)
v_mgr = []
for emp_list in emp_csv:
    if  emp_list[0] == '101':
        v_mgr.append(emp_list[3])

file = open("c:/r/emp.csv",'r')
emp_csv = csv.reader(file)
for emp_list in emp_csv:
    if emp_list[0] == v_mgr[0]:
        print(emp_list[1], emp_list[4], emp_list[5])
     
##SQL
#조인의 방법,데이터 엑세스 방법,데이터 분리이유?

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

s = Series([2,4,8,np.nan,6])
s.sum()
s.sum(skipna = True)
s.sum(skipna = False)
s.mean()
s.var()
s.std()
s.max()
s.min()
s.cumsum()
s.idxmin()
s.idxmax()
s[s.idxmin()]
s[s.idxmax()]
s.describe()
s.count()
len(s)


df = DataFrame([[60,80,70],[50,75,83],[90,83,81]],index = ['홍길동','박찬호','손흥민'],columns = ['영어','수학','국어'])

df.sum()
df.sum(axis = 0)
df.sum(axis = 1)
df.mean()
df.mean(axis =1)

제임스 영어(100),수학(np.nan)국어(90)


df.at['제임스','영어'] = 100
df.at['제임스','수학'] = np.nan
df.at['제임스','국어'] = 90

df.mean(axis =1)
df.mean(axis =1,skipna = False)
df.mean(skipna = False)
df.sum()
df.mean()

df.loc['홍길동'].sum()
df.describe()
df


[문제146] 최고 급여, 최저 급여 출력하세요.
import  pandas  as  pd
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
emp.describe()
emp['sal'].max()
emp['sal'].min()

[문제147] 20번 부서 사원들의 급여 합을 구하세요

emp['sal'][emp['deptno']==20].sum()

[문제148] 부서번호를 입력하면 그 부서의 급여 총액을 구하는 함수를 생성하세요.

dept_sum_sal()
부서번호를 입력하세요 :  20
19000.0

dept_sum_sal()
부서번호를 입력하세요 :  30
24900.0

def dept_sum_sal():
    x = int(input("부서번호를 입력하세요 : "))
    print(emp['sal'][emp['deptno']==x].sum())



[문제149] 직업을 물어보게하고 직업을 입력하면 해당 직업의 최고 급여를 출력되게하는데 아무것도 입력하지 않으면 계속 물어보게하는
프로그램을 작성하세요.

job_max_sal()
직업을 입력하세요 ?  ST_CLERK
3600.0

job_max_sal()
직업을 입력하세요 ? sa_rep
11500.0

job_max_sal()
직업을 입력하세요 ? 
직업을 입력하세요 ? 
직업을 입력하세요 ? 

job_max_sal()
직업을 입력하세요 ? sales
해당 직업의 사원은 없습니다.



def job_max_sal():
    x = input("직업을 입력하세요 ? ")
    x = x.upper()
    try:
        if x == "":
            job_max_sal()
        elif x not in str(emp['job']):
            raise Exception
        else:
            return print(emp['sal'][emp['job'] == x].max())
    except Exception:
        print("해당 직업의 사원은 없습니다.")

        
        
emp['sal'].sum()  #결과값이 numpy의 array형식으로 나온다. 1차원 형으로 값이 나온다.
emp[['sal']].sum()  #결과값이 시리즈형으로 나온다. 2차원 형으로 값이 나온다.
emp[['sal']].sum().values[0] #결과값을 인덱스를 제외하고 시리즈 결과값으로

##선생님
import pandas as pd

def job_max_sal():
    try:
        emp = pd.read_csv("c:\data\emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
        name = ''
        while name =='':
            name = input('직업을 입력하세요 ? ')
        maxsal = emp['sal'][emp['job'] == name.upper()].max()
        if pd.isnull(maxsal):
            raise Exception
        return maxsal
    except Exception as err:
        print ('해당 직업의 사원은 없습니다.')

job_max_sal()


