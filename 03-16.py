[문제150]부서번호,급여를 기준으로 내림차순 정렬해서 아래 화면처럼 컬럼정보를 출력하세요.

     deptno  empid         name      sal
105   110.0    205      Higgins  12008.0
106   110.0    206        Gietz   8300.0
8     100.0    108    Greenberg  13208.8
9     100.0    109       Faviet   9900.0
10    100.0    110         Chen   8200.0
12    100.0    112        Urman   7800.0
11    100.0    111      Sciarra   7700.0
13    100.0    113         Popp   6900.0

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

emp[["deptno","empid","name","sal"]].sort_values(by = ['deptno','sal'],ascending = False)

##    .astype()
s = Series(['1','2']) #문자형식으로 들어가면?
s.sum() #문자가 붙어서 나온다.
s.astype(int).sum() #스타일을 숫자로 처리

df = DataFrame(['1','2']) #문자형식으로 들어가면?
df.sum() #문자가 붙어서 나온다.
df.astype(int).sum() #스타일을 숫자로 처리

s = Series(['1','2','10']) #문자형식으로 들어가면?
s.sort_values() #문자가 붙어서 나온다.
s.sort_values(ascending = False) #문자가 붙어서 나온다.
s.astype(int).sort_values() #스타일을 숫자로 처리
s.astype(int).sort_values(ascending = False) #스타일을 숫자로 처리


[문제151] index 번호 0부터 50까지 부서번호, 급여를 기준으로 내림차순 정렬한 후 아래결과처럼 출력하세요.


    deptno  empid         name      sal
8    100.0    108    Greenberg  13208.8
9    100.0    109       Faviet   9900.0
10   100.0    110         Chen   8200.0
12   100.0    112        Urman   7800.0
11   100.0    111      Sciarra   7700.0
13   100.0    113         Popp   6900.0

from pandas import Series,DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

emp[["deptno","empid","name","sal"]][0:51].sort_values(by = ['deptno','sal'],ascending = False)


[문제152] 50번 부서 사원들의 정보를 급여를 기준으로 내림차순 정렬해서 해서 아래 화면처럼 컬럼정보를 출력하세요.

   empid         name  deptno     sal
21    121        Fripp    50.0  8200.0
20    120        Weiss    50.0  8000.0
22    122     Kaufling    50.0  7900.0
23    123      Vollman    50.0  6500.0
24    124      Mourgos    50.0  5800.0
84    184     Sarchand    50.0  4200.0


from pandas import Series,DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

emp[["deptno","empid","name","sal"]][emp["deptno"]==50].sort_values(by = ['deptno','sal'],ascending = False)


[문제153] 10,20,30,40,50번 부서 사원들의 급여의 총액을 출력하세요.

<화면출력>
10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0


from pandas import Series,DataFrame
import pandas as pd
import numpy as np

emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

##쌤꺼
deptno_dict = {}
for i in [10,20,30,40,50]:
    dept_sum = emp.loc[emp["deptno"]==i,'sal'].sum()
    deptno_dict[i] = dept_sum
    
for k,v in deptno_dict.items():
    print(k,v)

##내꺼 1
a = {}
for i in [10,20,30,40,50]:
    a[i] = emp[["deptno","sal"]][emp["deptno"]==i].sum().values[1]
for b,c in a.items():
    print(b,c)

##내꺼 2
a = {}
for i in [10,20,30,40,50]:
    a[i] = emp[["deptno","sal"]][emp["deptno"]==i].sum().values[1]
    print(int(i),a[i])


s = Series([1,2,3,4,1,2,3,4,1,2,5,6])

#유일한 값만 찾기

s.unique()
s.value_counts()
s.value_counts(normalize = True)  #상대비율
s.value_counts(sort = True)
s.value_counts(sort = False)

df = DataFrame({'a':['a1','a1','a1','a2','a2','a3'],'b':['b1','b1','b2','b2','b3',np.nan]})
df['a'].unique()
df['b'].unique()
df['b'].value_counts(dropna = True)



[문제154] 부서별로 급여 총액을 출력하세요.

<화면 출력>

10 4400.0
20 19000.0
30 24900.0
40 6500.0
50 156400.0
60 28800.0
70 10000.0
80 304500.0
90 58000.0
100 53708.8
110 20308.0

emp = pd.read_csv("c:/r/emp.csv", names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])

import math

dept = emp['deptno'].dropna().unique()
dept.sort()

deptdict = {}
for i in dept:
    deptsum = emp.loc[emp["deptno"]==i,'sal'].sum()
    deptdict[i] = deptsum
    
for k,v in deptdict.items():
    print(math.trunc(k),v)
    
    

dept = emp['deptno'].dropna().unique()
dept.sort()
a = {}
for i in dept:
    a[i] = emp[["deptno","sal"]][emp["deptno"]==i].sum().values[1]
    print(int(i),a[i])


emp.shape
emp.columns
emp.dtype


emp2 = emp[['empid','name','job','deptno']]
emp2
emp2.head()
emp2.tail()
emp2['deptno'].unique()

##groupby(열을 기준으로)묶는다.
emp['sal'].groupby(emp['deptno']).sum()


deptno_group = emp['sal'].groupby(emp['deptno'])

deptno_group.sum()
deptno_group.mean()
deptno_group.var()
deptno_group.std()
deptno_group.count()
deptno_group.max()
deptno_group.min()


emp['sal'].groupby([emp['deptno'],emp['job']]).sum()
dept_group = emp['sal'].groupby([emp['deptno'],emp['job']])

dept_group.sum()
dept_mean = dept_group.mean()
dept_mean
dept_mean.unstack()

emp['sal'].groupby([emp['deptno'],emp['job']]).sum()
emp.groupby(['deptno','job'])['sal'].sum()

emp.groupby(['deptno','job'])['sal'].sum().unstack()
emp.groupby('deptno')

for name,group in emp.groupby('deptno'):
    print(name)
    print(group)

for (name1,name2),group in emp.groupby(['deptno','job']):
    print(name1,name2)
    print(group)

