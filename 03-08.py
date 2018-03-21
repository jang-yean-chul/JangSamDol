import time

#1970년 1월 1일 자정 이후 누적된 초
time.time()

# 초만큼 정지 시킨다.
time.sleep(10)

# 현재 시간
time.localtime()

t = time.time()
time.localtime(t)

tm_yday : 1월 1일부터 오늘까지 누적된 날짜(1~366)
tm_isdst : 일광적약 시간(서머타임) 0 , 1, -1

time.localtime().tm_yday
t1 = time.localtime()
t1.tm_mon

# UTF 기준의 표준시
time.gmtime()
time.gmtime(1234567890)

time.asctime()
time.ctime()

time.mktime(time.localtime())

time.strftime('%y %Y %m %B %b %d', time.localtime()) #2자리 년/4자리 년/ 숫자 월/문자 월/문자약어 월/일

time.strftime('%H %I %p %M %S', time.localtime()) #시/시/분/초/오전오후

time.strftime('%A %a %w', time.localtime()) 
#문자 요일 / 문자 약어 요일 / 숫자 요일  %w =  tm_wday값과는 다르게 월 : 1~일 : 0이다.
"""
%j : 1월 1일부터 누적된날짜 (1~366)
%c : 날짜,시간
%x : 월/일/년도
%X : 시:분:초
%W : 누적된 주(월요일 시작)
%U : 누적된 주 (일요일 시작)
%z : 시간대 (대한민국표준시)
"""
time.strftime('%x %X %W %U',time.localtime())

strftime : 시간 -> 문자열
strptime : 문자열 -> 시간
time.strptime('2018 7 8', '%Y %m %d')

##달력을 표시하는 모듈
import calendar

print(calendar.calendar(2018))
#년도의 달력
calendar.prcal(2019)
#달의 달력
calendar.prmonth(2018,5)
# 해당날짜의 요일
calendar.weekday(2018,3,8)
# 그달의 첫째날짜의 요일., 마지막 일
calendar.monthrange(2018,3)

■ csv
import csv
#open 은 메모리만 할당한다고 생각하면 된다.
file = open("c:\R\emp.csv","r")

emp_csv = csv.reader(file)

for emp_list in emp_csv:
    print(emp_list)
    
    
[문제 74] last_name, salary 출력하세요
file = open("c:\R\emp3.csv","r")

emp_csv = csv.reader(file)

for emp in emp_csv:
    print(emp[2],emp[7])  
    

[문제 75] last_name, last_name의 길이를 출력하세요

file = open("c:\R\emp3.csv","r")

emp_csv = csv.reader(file)

for emp in emp_csv:
    print(emp[2],len(emp[2])) 
    
[문제 76] employee_id, last_name, salary를 12달 곱한값을 출력하세요.

file = open("c:\R\emp3.csv","r")

emp_csv = csv.reader(file)

for emp in emp_csv:
    print(emp[0],emp[2],float(emp[7])*12) 

[문제 77] 이름과 커미션을 출력하는데 커미션 null 이면 0으로 출력하시오

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    if emp[8] == '':
        print(emp[2],0) 
    else:
        print(emp[2],emp[8]) 



def ifnull(var1,var2):
    if var1 =='':
        return var2
    return var1

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
        print(emp[2],ifnull(emp[8],0))


[문제78] 이름은 대문자로 직업은 소문자로 출력하세요.

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    print(emp[2].upper(),emp[6].lower())

[문제 79] 이름 첫글자만 추출해서 소문자로 출력하세요

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    print(emp[2][0].lower())

[문제 80]이름의 두번째부터 마지막까지 추출해서 소문자로 출력하세요.

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    print(emp[2][1:len(emp[2])].lower())




file = open("c:\R\emp.csv","r")
emp_csv = csv.DictReader(file)
for emp in emp_csv:
    print(emp["LAST_NAME"])
    
    
[문제 81]이름을 입력하면 첫번째 철자는 대문자 나머지는 소문자로 출력하는 
initcap 함수를 생성한후 initcap함수를 이용해서 이름을 출력하세요.

initcap('james')
    
def initcap(arg):
    return arg[0].upper()+arg[1:].lower()
                 
[문제 82]이름을 입력하면 제일 뒤에 있는 철자는 대문자 앞의 문자는 소문자로
출력하는 tailcap 함수를 생성하세요.

    
tailcap('james')

def tailcap(arg):
    return arg[0:len(arg)-1].lower()+arg[-1].upper()


[문제 83]이름의 첫번째 철자부터 세번째 철자까지 출력하세요

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    print(emp[2][0:3])


[문제 84]이름 뒤에서 두글자만 출력하세요


file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    print(emp[2][-3:-1])


[문제 85]이름과 급여를 출력하는데 월급을 출력할 때에 0대신 *를 출력하시오!

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    print(emp[2],emp[7].replace('0',"*"))
    
[문제86] 문제 85번 결과를 새로운 sal 변수에 넣어 주세요

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
sal = []
for emp in emp_csv:
    sal.append(emp[7].replace('0','*'))
sal

■ round 함수
round(45.926,0)
46.0
round(45.926,1)
45.9
round(45.926,2)
45.93
round(45.926,-1)
50.0


■ math.trunc() 함수 math 모듈 #r, sql과 다르게 소숫점 자리 무조건 버림

math.trunc(15.926)

[문제87] 이름, 급여, 보너스를 출력하는데 보너스는 급여의 15% 출력해주세요. 
	단 보너스는 소숫점은 버리세요.

import math

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    print(emp[2],emp[7],math.trunc(float(emp[7])*0.15))

[문제 88]이름, 입사한요일(한글)을 출력하세요.

file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    week = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    print(emp[2],week[int(time.strftime('%w',time.strptime(emp[5],'%y/%m/%d')))])
    
[문제 89]이름, 입사한 날짜로부터 오늘까지 총 몇일 근무했는지 출력하세요.


###윤달의 차이가 있다.
file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    days = ((time.localtime().tm_year-time.strptime(emp[5],'%y/%m/%d').tm_year)*365) - time.strptime(emp[5],'%y/%m/%d').tm_yday + time.localtime().tm_yday
    print(emp[2],days)


file = open("c:\R\emp3.csv","r")
emp_csv = csv.reader(file)
for emp in emp_csv:
    a = time.mktime(time.localtime()) - time.mktime(time.strptime(emp[5],'%y/%m/%d'))
    print(emp[2],math.trunc(a/86400))


