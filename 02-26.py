# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('오늘도 행복하자')
# F9를 눌러야 실행됨

"""
 #변수
 - 메모리 포인터
 - 첫글자는 영문, _(밑줄)
 - 두번째 글자부터 영문자, 숫자, _
 - 대소문자 구분
 - 길이 제약 없음
 - 예약어는 사용 할 수 없다.
     예약어 확인 방법 = import keyword
 """
keyword.kwlist  #예약어list 이므로 여기있는 것들은 변수로 사용 불가.

x = 10
type(x) # type 확인 (int = 정수[양의 정수, 음의 정수, 0])

# 사칙 연산
2+1  #덧셈
2-1  #뺄셈
2*2  #곱셈
2/2  #나눗셈
7//2  #나누기 몫
7%2  #나누기 나머지
2**3  #승의 곱

# import math
math.pow(2,3)  #2의 3승

(1+2)*3*2**3

a = 1
a = a+1

#연산자 축약으로 사용
a = a+1
a += 1

a = a-1
a -= -1

a = a*2
a *= 2

a = a/2
a /= 2

type(a)

f = 10.12    # type(f) => 부동소숫점(float)

f = 10.4e-3 # e 지수 표현 10.4*10**-3  type(f)

#   y < x 
#   y <= x
#   x == y
#   x != y

2>1 and 3>2
2>1 and 3<2
2>1 or 3<2
not 1>2

"""
[문제1] x,y 변수에 있는 값을 기준으로 수행한 결과 입니다. 
x 와 y 변수에 어떤 값이 있어야 하나요.
또한 결과값이 나오기 위해서 어떤 계산식을 만들어야 하는지 계산식을 만들어 보세요.

result_1 =  7
result_2 =  3
result_3 =  -3
result_4 =  10
result_5 =  0.4
result_6 =  0
result_7 =  2
result_8 =  32
result_9 =  7.0
result_10 =  -21
result_11 =  50
result_12 =  29
"""
x = 2
y = 5

x+y
y-x
x-y
x*y
x/y
x//y
x % y
x ** y
(x + ((x*y)/x))
(x+y)*(x-y)
x * (y**x)
(x**2) + (y**2)


'''
문자열

작은 따옴표 '대한민국'
큰 따옴표 "대한민국"
'''

'''대한민국
대한민국'''

## escape 문자

# \n : 줄 바꾸기
print('대한민국\n대한민국')

# \t : tab key
print('잘하자\t파이썬')

# \0 : null
print('잘하자\0파이썬')

# \\ : \표시
print('잘하자\\파이썬')

# \' : 단일 인용부호
print('잘하자\'파이썬\'')
print("잘하자'파이썬'")


x = '김태효'
y = 'UFC'

type(x) 
x + y
(x + y) *2

print("="*15)
print("Hello world")
print("="*15)

s1 = 'R'
s2 = 'PYTHON'

print("나는 %s전문가입니다. 지금은 %s공부에 빠져있습니다."%(s1,s2))

n1 = 100
n2 = 200
print("%d + %d = %d" %(n1,n2,n1+n2))

print("지금 행복지수는 작년에 비해 %d%%증가했습니다"%n2)

#인덱싱 & 슬라이싱
x = "행복한 하루 보내자"

len(x)

x[:]
x[0]
x[1]
x[len(x)-1]  #0부터 시작하므로 마지막 글자를 뽑아내려면 -1을 해주어야 한다.
x[-1]  #뒤에서부터는 정상적으로 -1부터 시작
x[0:3] #[시작번호:끝번호]
x[3:]
x[:3]
x[:-1] # -를 뒤에 쓸 경우 해당 글자는 제외하고 보여준다.




#[문제_2] v_str 변수에 이 문자열을 입력하세요. 
v_str = "시간은 멈추지 않습니다. 하루를 유익하게 살아야합니다."

#1. "시간은 멈추지 않습니다." 만 출력해주세요
v_str[0:13]

#2. "하루를 유익하게 살아야합니다." 만 출력해주세요
v_str[14:len(v_str)-1]

#3. "살아야합니다."  만 출력해주세요
v_str[23:len(v_str)-1]

#4. "시추니루하야"  이 글자만 출력해주세요.
v_str[0]+v_str[5]+v_str[10]+v_str[15]+v_str[20]+v_str[24]

#5. "시간은 멈추지 않습니다. 하루를 유익하게" 만 출력해주세요.
v_str[0:-8]

#6. v_str 문자열을 뒤순으로 출력해 주세요.
v_str[::-1]



#[문제_3] 

x = '파리썬'
x

# 인덱스를 이용해서 리 -> 이로 변환하세요.
x = x[0]+"이"+x[2]
x      
    
  
#[문제_4] 포맷문자를 이용해서 출력하세요.
#1. 안녕하세요. {제임스} 입니다. 즐겨듣는 음악은 {클래식} 입니다.
print("안녕하세요. %s 입니다. 즐겨듣는 음악은 %s 입니다."%("제임스","클래식"))
"안녕하세요. {} 입니다. 즐겨듣는 음악은 {} 입니다.".format("제임스","클래식")
#2. {996} 를 {8} 나누면 {4} 가 나머지입니다
print("%s 를 %s 나누면 %s 가 나머지 입니다."%(996,8,996%8))
#3. {996} 를 {8} 나누면 {124}는 몫이고 {4} 나머지입니다
print("%s 를 %s 나누면 %s는 몫이고 %s 나머지 입니다."%(996,8,996//8,996%8))


print("원주율은 %d 입니다."%3.14159)   # %d는 정수이므로. 3만 나온다. 
print("원주율은 {} 입니다.".format(3.14159))
print("원주율은 %f 입니다."%3.14159)

##문자합수

x = "hello world"
    # startswith() : 원본 문자열이 매개변수로 입력한 문자열로 시작되는지를 판단. 

x.startswith('he')
x.startswith("H")
    # endswith() : 원본 문자열이 매개변수로 입력한 문자열로 끝나는지를 판단.
x.endswith("ld")
x.endswith("D")

    # find() : 원본 문자열안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에부터 찾는다.
                만약에 존재하지 않으면 -1 로 나온다.
x.find("w")
x.find("world")
x.find("h")

    # rfind() : 원본 문자열안에 매개변수로 입력한 문자열이 존재하는 위치를 뒤에서부터 찾는다.
x.rfind("w")
x.rfind("h")

    # count() : 원본 문자열 안에 매개변수로 입력한 문자열이 몇번 나오는지에 대한 건수
x.count("l")


x = '      hello     '


    # lstrip() : 원본 문자열 왼쪽에 공백을 제거
x.lstrip()
    # rstrip() : 원본 문자열 오른쪽에 공백을 제거
x.rstrip()
    # strip() : 원본 문자열 양쪽에 공백을 제거
x.strip()


x = "hello"
y = "hello2018" 
z = "안녕하세요"

    # isalpha() : 원본 문자열이 숫자, 기호를 제외한 알파벳, 한글로 이루어져있는지 확인.    
x.isalpha()
y.isalpha()
z.isalpha()


    # isalnum() : 원본 문자열이 알파벳,숫자로 이루어져 있는지 확인.
x.isalnum()
y.isalnum()
z.isalnum()

    # isnumeric() : 원본 문자열이 수로만 이루어져 있는지 확인.

x.isnumeric()
y.isnumeric()
z.isnumeric()

x = "hello world"

    # replace() : 원본 문자열에서 어떤 문자열을 찾아서 새로운 문자열로 변경
x.replace("world","python")


x= "파리썬"
x = x.replace("리","이")
x


x = "hello, world"
    # split() : 매개변수로 입력한 문자열을 기준으로 원본 문자열을 나눠 리스트로 만든다.
x.split(",")


    # upper() : 원본 문자열을 대문자로 변환
x.upper()

    # lower() : 원본 문자열을 소문자로 변환
x.lower()

    # index() : 원본 분자열 안에 매개변수로 입력한 문자열이 존재하는 위치를 앞에서 부터 찾는다.
    #           find와의 차이점은 index는 없으면 오류가 난다.
x.index('o')
x.index("O")

    # in : 문자열이 존재하는지를 확인
'o' in x


#[문제5] 
#alha = 'aAbBcCdDeEfFgGhHiIjJkK' 변수에 값이 들어 있습니다. 
#화면의 결과는  ABCDEFGHIJK 출력하세요.
alha = 'aAbBcCdDeEfFgGhHiIjJkK'
alha[1::2]

#[문제6] 

#a = 'a b c d e f g' 변수에 문자열이 들어 있습니다. 다음을 수행하세요.
a = 'a b c d e f g'

#1. a 변수에 있는 문자의 갯수를  구하세요.
len(a)

#2. a 변수에 공백문자 갯수를 구하세요.
x = len(a)
y = len(a.replace(" " ,""))

x-y 

#3. a 변수 안에 있는 공백문자를 제외한 갯수를 구하세요.
len(a.replace(" ",""))

#4. a 변수에 있는 공백문자를 제거한 후 b 변수에 넣어주세요
a = 'a b c d e f g'
b = a.replace(" ", "")
b
#5. a 변수에 있는 문자를 분리한 후 c 변수에 넣어주세요.
c = a.split(" ")
c
type(c)   # list 형식

c = ','.join(c)
type(c) # str 형식으로 변경

x = 'abc'
x = ','.join(x)     # x라는 변수의 문자열 사이사이에 ,를 끼워 넣겠다는 뜻
x
