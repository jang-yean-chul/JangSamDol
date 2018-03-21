[문제90] 오늘부터 이번달 말일까지 몇일 남았는지 출력하세요.

import datetime

now=datetime.date.today()
now
lastday=datetime.date(2018,3,31)
lastday
dt=lastday-now
dt.days


[선생님]

from datetime import date
from calendar import monthrange

monthrange(2018,3)[0] 	#첫째 날의 요일을 숫자로 출력
monthrange(2018,3)[1] 	#그달의 마지막 날짜를 출력

monthrange(2018,3)[1] - date.today().day

Out[63]: 22



[문제91] 사원번호가 100번 사원의 사원이름과 급여를 출력하세요.

import csv

file=open("c:\R\emp.csv","r")
emp_csv=csv.reader(file)

for i in emp_csv:
    if i[0] == '100':
        print(i[2],i[7])

King 35138.4

[R]

emp<-read.csv("c:/R/emp_d.csv",header =T, stringsAsFactors=F)
emp

emp[emp$EMPLOYEE_ID==100,c("LAST_NAME",'SALARY')]


[문제92] 급여가 10000 이상인 사원들의 이름과 급여를 출력하세요.


import csv
file=open("c:\R\emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if float(i[7]) >= 10000:
        print(i[2], i[7])
>
King 35138.4
Kochhar 22627
De Haan 24889.7
Greenberg 12008
Raphaely 11000
Russell 14000
Partners 13500
Errazuriz 12000
Cambrault 11000
Zlotkey 10500
Tucker 10000
King 10000
Vishney 10500
Ozer 11500
Bloom 10000
Abel 11000
Hartstein 13000
Baer 10000
Higgins 12008


[문제93] 2001-01-13 일에 입사한 사원의 이름과 입사일을 출력하세요

import datetime        
import csv

file=open("c:\R\emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    date = time.strptime(i[5],"%y/%m/%d") 
    if date == time.strptime('2001-01-13',"%Y-%m-%d"):
        print(i[2],i[5])


[문제94] 2002년도에 입사한 사원들의 이름과 입사일을 출력하세요

file=open("c:\R\emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    date=time.strptime(i[5],'%y/%m/%d')
    if date.tm_year == 2002:
        print(i[2],i[5])

Greenberg 02/08/17
Faviet 02/08/16
Raphaely 02/12/07
Mavris 02/06/07
Baer 02/06/07
Higgins 02/06/07
Gietz 02/06/07


file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
	if time.strptime(emp_list[5],"%y/%m/%d").tmyear == 



[선생님]

import datetime  

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for emp_list in emp_csv:
    if time.strptime(emp_list[5],"%y/%m/%d").tm_year == time.strptime('2002',"%Y").tm_year:
        print (emp_list[2],emp_list[5])


[문제 95] job이 ST_CLERK이고 월급 300 이상인 사원들의 이름과 JOB, 급여 출력하세요.
file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if (i[6] == 'ST_CLERK') and (float(i[7]) >= 300):
        print (i[2],i[6],i[7])
>
ST_CLERK 3200
ST_CLERK 2700
ST_CLERK 2400
ST_CLERK 2200
ST_CLERK 3300
ST_CLERK 2800
ST_CLERK 2500
ST_CLERK 2100
ST_CLERK 3300
ST_CLERK 2900
ST_CLERK 2400
ST_CLERK 2200
ST_CLERK 3600
ST_CLERK 3200
ST_CLERK 2700
ST_CLERK 2500
ST_CLERK 3500
ST_CLERK 3100
ST_CLERK 2600
ST_CLERK 2500

[문제 96] 급여가 2500에서 3000사이인 사원들의 이름과 급여를 출력하세요.

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if float(i[7]) >= 2500 and float(i[7])<=3000:
        print (i[2],i[7])
>
Mikkilineni 2700
Atkinson 2800
Marlow 2500
Rogers 2900
Seo 2700
Patel 2500
Matos 2600
Vargas 2500
Sullivan 2500
Geoni 2800
Cabrio 3000
Gates 2900
Perkins 2500
Jones 2800
Feeney 3000
OConnell 2600
Grant 2600

[문제 97] JOB이 AD+VP, AD_PRES인 사원들의 이름과 월급과 직업을 출력하세요.

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[6] == 'AD+VP' or i[6] == 'AD_PRES':
        print (i[6],i[7])
>
AD_PRES 24000



[선생님] # in 연산자 사용

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[6] in ['AD+VP','AD_PRES']:
        print (i[2],i[6],i[7])


[문제 98] 직업이 AD_VP, AD_PRES이 아닌 사원들의 이름과 월급과 직업을 출력하세요

import csv

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[6] not in ['AD_VP','AD_PRES']:
        print(i[2],i[6],i[7])
    
[문제 99] 커미션이 null인 사원들의 이름,급여,커미션을 출력하세요

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[8] == '':
        print(i[2],i[7],i[8])
>  
Mavris 6500 
Baer 10000 
Higgins 12008 
Gietz 8300 
...

[문제 100] 커미션이 null이 아닌 사원들의 이름, 급여 커미션을 출력하세요.

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[8] != "":
        print(i[2],i[7],i[8])
>
Taylor 8600 0.2
Livingston 8400 0.2
Grant 7000 0.15
Johnson 6200 0.1
...

[문제 101] last_name의 첫번째 철자가 S로 시작하는 사원들의 이름과 급여를 출력하세요

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[2][0] == "S":
        print(i[2],i[7])
>
Sciarra 7700
Stiles 3200
Seo 2700
Sully 9500
...


[문제 102] last_name의 두번째 철자가 i 인 사원들의 이름과 월급을 출력하세요.

file = open("c:/data/emp.csv","r")
emp_csv=csv.reader(file)
for i in emp_csv:
    if i[2][1] == "i":
        print(i[2],i[7])

>
King 24000
Himuro 1000
Mikkilineni 2700
Bissot 3300

import csv
[문제 103]이름, 급여 출력하는데 이름이 오름차순으로 출력하세요.

##내꺼
file = open("c:/r/emp3.csv","r")
emp_csv=csv.reader(file)
data = []
for i in emp_csv:
    data.append([i[2],i[7]])
data.sort()
print(data)

##선생님꺼
file = open ("c:/r/emp3.csv","r")
emp = csv.reader(file)
data = []
for i in emp:
    data.append(i)

def sortCheck(arg):
    return(arg[1])
#데이터 안에 정렬시킬 대상의 인덱스번호를 입력 여기서는 이름이므로 1을 입력
data_sorted = sorted(data,reverse = False,key = sortCheck)
#key에 해당하는 값은 내가 직접 함수를 짜서 넣어야 한다.

for i in data_sorted:
    print(i[1],i[7])
"""
■ 람다(lambda) 함수
 - 이름이 없는 한 줄짜리 함수
 - 가독성을 위해서
 - 함수를 인수로 넘겨 줄 때
"""
def f1 (x,y):
    return x*y

f1(2,3)

(lambda x, y : x*y)(2,3)

f1 = lambda x,y : x*y
f1(2,3)


### lambda를 이용해서 해결
file = open ("c:/r/emp3.csv","r")
emp = csv.reader(file)
data = []
for i in emp:
    data.append(i)

data_sorted = sorted(data,reverse = False,key = lambda data : data[1])

for i in data_sorted:
    print(i[1],i[7])

##정렬하는 방법!!!
from operator import itemgetter

file = open ("c:/r/emp3.csv","r")
emp = csv.reader(file)
data = []
for i in emp:
    data.append(i)
    
for i in range(len(data)):
    data[i][7] = float(data[i][7])

data_sorted = sorted(data,reverse = False,key = itemgetter(1,7))

for i in data_sorted:
    print(i[1],i[7])


[문제104]Job ST_CLERK 인 사원들의 이름과 입사일과 Job을 출력하는데 가장 최근에 입사한 사원부터 출력하세요.

file = open ("c:/r/emp3.csv","r")
emp = csv.reader(file)
data = []

for i in emp:
    data.append(i)

data_sorted = sorted(data,reverse = False, key = itemgetter(5))

for i in data_sorted:
    if i[6] == 'ST_CLERK':
        print(i[1],i[5],i[6])
        
        
[문제 105] 부서별 급여의 총액을 구하세요.
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
        if j[10] == i:
            tosal += float(j[7])
    print(i, tosal)


import csv
file = open ("c:/r/emp2.csv","r")
emp = csv.reader(file)
dept_sum = {}
for i in emp:
    if i[10] in dept_sum:
        dept_sum[i[10]] = float(dept_sum[i[10]]) + float(i[7])
    else:
        dept_sum[i[10]] = float(i[7])

for k,v in dept_sum.items():
    print(k,v)
