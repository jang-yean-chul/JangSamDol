from statistics import *
dir()

stdev([1,2,3,4,5]) # 인자값 하나만 들어갈수있는것 
stddev(1,2,3,4,5)

if __name__=="__main__":
    print(stddev(1,2,3,4,5))


[문제69]프로그램을 생성하세요.

액수입력 : 362
화폐단위를 입력하세요 : 100 50 1
1원 : 12개
50원 : 1개
100원 : 3개

##내꺼 1번
def exchange():
    cost = int(input("액수입력 : "))
    d = input("화폐단위를 입력하세요 : ")
    d2 = d.split(" ")
    x = [] 
    for i in range(len(d2)):
        x.append(int(d2[i]))
    x.sort(reverse = True)
    
    g = []
    h = []
    for i in range(len(x)):
        g.append(cost // x[i])
        h.append(cost % x[i])
        cost = h[i]
    
    x.reverse()
    g.reverse()
    for i in range(len(x)):
        print(x[i],"원 : ",g[i],"개")


##내꺼 2번
def exchange():
    cost = int(input("액수입력 : "))
    d = [int(x) for x in input("화폐단위를 입력하세요 : ").split(' ')]
    d.sort(reverse = True)
    
    h = []
    for i in range(len(d)):
        dvmd = divmod(cost,d[i])
        cost = dvmd[1]
        h.append(dvmd[0])
        
    d.reverse()
    h.reverse()
    
    for i in range(len(d)):
        print("{}원 : {}개".format(d[i],h[i]))
    
    
##내꺼 3번
def exchange():
    cost = int(input("액수입력 : "))
    d = [int(x) for x in input("화폐단위를 입력하세요 : ").split(' ')]
     
    for i in d:
        g = cost // i 
        h = cost % i
        cost = cost % i
        print("{}원 : {}개".format(i,g))

exchange()


dvmd = divmod(362,100)
dvmd

##선생님꺼 
def coinGreedy(money, cash_type):
    cash_type.sort(reverse = True)
    remain = money
    res = {}
    for cash in cash_type:
        dvmd = divmod(remain, cash)
        
        res[cash] = dvmd[0]
        
        remain = dvmd[1]
        
    return res

money = int(input("액수입력 : "))
cash_type = [int(x) for x in input("화폐단위를 입력하세요 : ").split(' ')]
res = coinGreedy(money, cash_type)
for k,v in res.items():
    print("{0}원 : {1}개".format(k,v))


■ 예외사항 처리
def divide(x,y):
    return x/y

divide(10,2)
divide(10,'둘')

#1
try:
    z = divide(10,0)
    print(z)
except:
    print("오류가 발생했습니다.")

#2  
try:
    z = divide(10,0)
    print(z)
except TypeError:
    print("인수값을 숫자로 입력하세요.")
except ZeroDivisionError:
    print("0값으로 나눌 수 없습니다.")
except:
    print("오류가 발생했습니다.")
else:   #위에서 except처리가 안됐을때 이 구문을 실행
    print("결과 : {}".format(z))
finally:    #무조건 마지막에 이거는 실행!
    print("프로그램 종료")


try:
    z = divide(10,'둘')
    print(z)
except TypeError:
    print("인수값을 숫자로 입력하세요.")
except ZeroDivisionError:
    print("0값으로 나눌 수 없습니다.")
except:
    print("오류가 발생했습니다.")
else:   #위에서 except처리가 안됐을때 이 구문을 실행
    print("결과 : {}".format(z))
finally:    #무조건 마지막에 이거는 실행!
    print("프로그램 종료")


def func(arg):
    try:
        if arg < 1 or arg > 10:
            raise Exception("유효하지 않은 숫자입니다. : {}".format(arg))
        else:
            print("입력한 수는 {} 입니다.".format(arg))
    except Exception as error:
        print("오류가 발생했습니다. {}".format(error))

func(5)
func(100)



[문제70] 숫자를 입력값으로 받은 후 짝수인지 홀수 인지를 출력한후 그 숫자값을 기준으로
짝수면 짝수형식의 증가값으로 10개 출력, 홀수면 홀수형식의 증가값으로 10개 출력합니다.
만약에 숫자가 들어 오지 않으면 예외사항 처리하세요.

숫자를 입력해주세요 : 10
짝수
10
12
14
16
18
20
22
24
26
28

숫자를 입력해주세요 : 11
홀수
11
13
15
17
19
21
23
25
27
29

숫자를 입력해주세요 : 이십
invalid literal for int() with base 10: '이십'
숫자를 입력하세요
 


def aaa():
    try:
        arg = int(input("숫자를 입력해 주세요 : "))
        if arg % 2 ==0:
            print("짝수")
            for i in range(10):
                print(arg)
                arg = arg+2
        else:
            print("홀수")
            for i in range(10):
                print(arg)
                arg = arg+2
    
    except ValueError as error:
        print(error)        
    
    finally:
        print("숫자를 입력하세요.")

aaa()

■ 날짜
import datetime

datetime.date.today()

d=datetime.date.today()

d.year
d.month
d.day
d.hour
d.minute
d.second
d.microsecond
d.date()
d.time()
d.weekday() # 0:월,6:일

datetime.date(2018,3,7)

d1 = d.replace(year = 2019, month = 3, day = 10)
d1

dt = datetime.datetime.now()
dt


[문제71] 오늘이 무슨 요일인지 출력해주세요.
def today_week():
    d = datetime.date.today()
    week = ['월','화','수','목','금','토','일']
    return week[d.weekday()]

today_week()

d=datetime.datetime.now()

d.strftime("%Y %m %d %H %M %S %A %B")

datetime.datetime.strptime('2018-03-07 15:48:00','%Y-%m-%d %H:%M:%S')


from datetime import date,time,datetime

d = date(2018,3,7)
t = time(15,53,00)

datetime.combine(d,t)

from datetime import timedelta, date
d = date.today()
td = timedelta(days = 100)
d + td


[문제72] 함수에 인수값으로 현재날짜, 일수 정보를 입력하면 더한 날짜정보가 리턴하는 next_day함수를 생성하세요.

from datetime import *

def next_day(y,m,d,num):
    try:
        d = date(y,m,d)
        td = timedelta(days = num)

        return d+td
    except ValueError as error:
        print(error)

    
        
next_day(2018,5,20,174091)


from datetime import timedelta,date
    
def next_day(arg1,arg2):
    return (arg1 + timedelta(days = arg2))

print(next_day(date.today(), 100))

import datetime
dt1 = datetime.datetime(2018,3,7,16)
dt2 = datetime.datetime(2018,2,7,16)



[문제73] 아래와 같은 결과가 출력될수 있도록 프로그램을 생성하세요


1에서 천만까지 짝수합, 홀수합 구합니다
1에서 천만까지 짝수합: 24999995000000
1에서 천만까지 홀수합: 25000000000000
처리시간 : 0:00:01.950003
처리시간 millisecond(1/1000)  : 1950ms

def aaa():
    start = datetime.now()
    print("1에서 천만까지 짝수합, 홀수합 구합니다")
    
    e = 0
    o = 0
    for i in range(10000000):
        if i % 2 ==0:
            e += i
        else:
            o += i
    print("1에서 천만까지 짝수합: ",e)
    print("1에서 천만까지 홀수합: ",o)
    end =datetime.now()-start
    print("처리시간 :" ,end)
    end_ms = int(end.total_seconds() * 1000)
    print("처리시간 millisecond(1/1000)  : ", end_ms,"ms")

aaa()
        
##############################
[문제73] 아래와 같은 결과가 출력될수 있도록 프로그램을 생성하세요


1에서 천만까지 짝수합, 홀수합 구합니다
1에서 천만까지 짝수합: 24999995000000
1에서 천만까지 홀수합: 25000000000000
처리시간 : 0:00:01.950003
처리시간 millisecond(1/1000)  : 1950ms
from datetime import datetime
start = datetime.now()
print('1에서 천만까지 짝수합, 홀수합 구합니다')
even_result = 0
odd_result = 0
for i in range(10000000):
    if i % 2 == 0:
        even_result += i
    else:
        odd_result += i
print('1에서 천만까지 짝수합: %d'%even_result)
print('1에서 천만까지 홀수합: %d'%odd_result)
end = datetime.now()
delta = end - start
print("처리시간 : ",delta)
delta_ms = int(delta.total_seconds() * 1000)
print("처리시간 millisecond(1/1000)  : %dms"%delta_ms)
###################################################

