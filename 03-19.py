[문제160] emp.csv 파일  데이터에 커미션 정보를 분석하려 합니다.
              커미션에 null값들의 수, null이 아닌값들의 수를 구하세요.


import csv

file = open("c:/r/emp.csv",'r')
emp= csv.reader(file)
cn = 0
for i in emp:
    if i[6] != '':
        cn += 1
print(cn)

file = open("c:/r/emp.csv",'r')
emp= csv.reader(file)
cn = 0
for i in emp:
    if i[6] == '':
        cn += 1
print(cn)



from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

emp["comm"].isnull().sum()
emp["comm"].notnull().sum()

print(emp[emp["comm"].notnull()]['empid'].count())
print(emp[emp["comm"].isnull()]['empid'].count())

[문제161] emp.csv, dept.csv 파일 데이터를 이용해서  조인된 결과를 보려고 합니다.
              조인 함수를 생성하세요.
 
join(emp,'deptno', dept,'deptno')
join(emp,'mgr', emp,'empid')
    
 
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:/r/dept.csv", names = ['deptno','deptname','mgr','locno'])

def join(arg1,arg2,arg3,arg4):
    return pd.merge(arg1,arg3, left_on = arg2,right_on = arg4)


#####
file = open("c:/r/emp.csv",'r')
emp_csv = csv.reader(file)
emp=[]
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2],'mgr':i[3],'hire_date':i[4],'sal':i[5],'comm':i[6],'deptno':i[7]})

file = open("c:/r/dept.csv",'r')
dept_csv = csv.reader(file)
dept=[]
for i in dept_csv:
    dept.append({'deptno':i[0],'deptname':i[1],'mgr':i[2],'loc':i[3]})

def join(arg1,arg11,arg2,arg22):
    for e in arg2:
        for d in arg1:
            if e[arg11] == d[arg22]:
                print(e,d)
    
join(emp,'deptno', dept,'deptno')
join(emp,'mgr', emp,'empno')



[문제162] 사원번호를 입력하면 부서이름을 리턴해주는 함수를 생성하세요.

print(dept_name_find(184))

Executive

## 1
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:/r/dept.csv", names = ['deptno','deptname','mgr','locno'])


def dept_name_find(num):
    a = pd.merge(emp,dept,on = 'deptno')
    return a['deptname'][a['empid']==num]
    


## 2
file = open("c:/r/emp.csv",'r')
emp_csv = csv.reader(file)
emp=[]
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2],'mgr':i[3],'hire_date':i[4],'sal':i[5],'comm':i[6],'deptno':i[7]})

file = open("c:/r/dept.csv",'r')
dept_csv = csv.reader(file)
dept=[]
for i in dept_csv:
    dept.append({'deptno':i[0],'deptname':i[1],'mgr':i[2],'loc':i[3]})


def dept_name_find(num):
    for i in emp:
        if int(i['empno']) == num:
            for d in dept:
                if i['deptno'] == d['deptno']:
                    return d['deptname']


[문제163] emp.csv, dept.csv 파일 데이터에서 50번 부서 사원의 중에 급여가 5000 이상인 사원의 이름, 부서 이름을 출력하세요.

file = open("c:/r/emp.csv",'r')
emp_csv = csv.reader(file)
emp=[]
for i in emp_csv:
    emp.append({'empno':i[0],'ename':i[1],'job':i[2],'mgr':i[3],'hire_date':i[4],'sal':i[5],'comm':i[6],'deptno':i[7]})

file = open("c:/r/dept.csv",'r')
dept_csv = csv.reader(file)
dept=[]
for i in dept_csv:
    dept.append({'deptno':i[0],'deptname':i[1],'mgr':i[2],'loc':i[3]})


for i in emp:
    if float(i['sal']) >= 5000 and i['deptno'] == '50':
        for j in dept:
            if i['deptno'] == j['deptno']:
                print(i['ename'],j['deptname'])


for d in dept:
    if d['deptno'] == '50':
        for e in emp:
            if (e['deptno'] == d['deptno']) & (float(e['sal']) >= 5000):
                print(e['ename'],e['sal'],d['deptname'])


  
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:/r/dept.csv", names = ['deptno','deptname','mgr','locno'])

emp.columns
dept.columns

#pandas의 merge는 join이다!
pd.merge(emp,dept,on = 'deptno')   #컬럼이름이 동일할 경우
pd.merge(emp,dept,left_on = 'deptno',right_on = 'deptno')   #컬럼이름이 다를 경우 
pd.merge(emp,dept,on = 'deptno', how = 'left')
pd.merge(emp,dept,on = 'deptno', how = 'right')
pd.merge(emp,dept,on = 'deptno', how = 'outer')
pd.merge(emp,dept,on = 'deptno', how = 'inner')


dept_new = dept.ix[:10,['deptno','deptname']]
dept_new
dept_new = dept_new.set_index('deptno')     #인덱스 넣기
dept_new
del dept_new.index.name  #인덱스지우기

pd.merge(emp,dept_new,left_on = 'deptno',right_index = True)


[문제164] emp.csv, dept.csv 파일 데이터에서 50번 부서 사원의 중에 급여가 5000 이상인 사원의 이름, 부서 이름을 출력하세요.(pandas이용하세요)

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:/r/dept.csv", names = ['deptno','deptname','mgr','locno'])

a = emp[['name','sal','deptno']][(emp['sal'] >= 5000)&(emp['deptno'] == 50)]
b = dept[['deptno','deptname']][dept['deptno'] == 50]

pd.merge(a,b,on = 'deptno')

[문제165] 2002년도에 근무한 사원들의 이름, 급여, 입사일, 부서코드,부서이름을 출력하세요.

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:/r/dept.csv", names = ['deptno','deptname','mgr','locno'])


a = pd.merge(emp,dept,on = 'deptno',how = 'left')

a[['name','sal','hire_date','deptno','deptname']][a['hire_date'].str.slice(0,4) == '2002']


[문제166] 직업이 AD_VP, AD_PRES 인 사원들의 이름, 급여, 직업, 부서코드, 부서이름 을 출력하세요.

from pandas import Series,DataFrame
import pandas as pd
import numpy as np
emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
dept = pd.read_csv("c:/r/dept.csv", names = ['deptno','deptname','mgr','locno'])

a = pd.merge(emp,dept,on = 'deptno',how = 'left')

a[['name','sal','job','deptno','deptname']][a['job'].isin(['AD_VP','AD_PRES'])]



from pandas import Series, dataFrame
import pandas as pd

data = Series(range(10),index = [['a','a','a','b','b','b','c','c','c','d'],[1,2,3,1,2,3,1,2,3,3]])
data.index  #MultiIndex가 나온다.
data['c']
data['b':'c']
data[:3]
data['a']
data.xs('a')
data.xs(('a',3))
data.xs('a',level = 0)
data.xs(3,level = 1)
data
data.unstack()
data.unstack().stack()

df = DataFrame(data)
df.index
df[0]
df.xs('a')
df.xs(('a',3))
df.xs('a',level = 0)
df.xs(3,level = 1)
