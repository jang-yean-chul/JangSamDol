##bool(부울) 자료형
#참(True), 거짓(False)을 나타내는 자료형.

x == y

1 == 1
2 > 1
1 >= 1
1 < 2
1 <= 1
1 != 2

not 1
not -1
not 0
not None

## 조건 제어식 할 때 중요하다.
# True 표현방법
bool(1)
bool(-1)
bool(0)
bool('python')      # 리터럴 문자값을 집어넣으면 무조건 True
bool([1,2,3])       # list 값을 집어넣으면 무조건 True
bool((1,2,3))       # tuple 값을 집어넣으면 무조건 True
bool({1,2,3})       # set 값을 집어넣으면 무조건 True

# False 표현방법
bool(0)
bool([])
bool({})
bool(())
bool(None)
bool('')

"""
■ 조건 제어문 , if문

if 조건문 : 스페이스바로 4칸을 무조건! 띄워야 한다.

if 조건문 : 
(1,2,3,4)수행해야할 문장
         수행해야할 문장
         
         
if 조건문 : 
(1,2,3,4)수행해야할 문장
         수행해야할 문장
else: 
         수행해야할 문장
         수행해야할 문장
"""
x= 10
if x==10:
    print("x는 10입니다.")  #여기까지하면 들여쓰기 오류 안남
  print('오늘 하루도 행복하자')  #들여쓰기 오류남
  
a = '참'
if a:
    print('참')
else:
    print('거짓')
    
a = []
if a:
    print('참')
else:
    print('거짓')

x = 2
if x > 10 and 1/x:
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')
    
x = 0
if x > 10 and 1/x:
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')   # 첫번쨰 조건이 False 이면 뒷조건을 무시한다.

x = 0
if x > 10 | 1/x:
    print('x는 10보다 크다')
else:
    print('x는 10보다 작다')   # 오류가 난다. 0으로 나누어서

# float, int, str

num = int(input('값을 입력해 주세요: '))

type(num)

score = int(input('점수 입력 : '))

if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

score
grade



#[문제12] 숫자를 입력값으로 받아서 짝수인지 홀수인지를 출력하는 프로그램을 만드세요.
number = int(input('숫자를 입력해 주세요 : '))

if number%2 == 1:
    print("홀수 입니다.")
else:
    print("짝수 입니다.")


#[문제13]한글, alphabet만 입력받아야 합니다. 
#       만약에 다른 문자가 들어 오면 "한글, alphabet 이외의 문자가 포함되어 있습니다." 라는 문구가 출력해야 하고 아니면 입력받은 문자를 출력하세요.

letter = str(input('영어 또는 한글을 입력해 주세요 : '))

if letter.isalpha() == True:
    print(letter)
else:
    print("한글, alphabet 이외의 문자가 포함되어 있습니다." )


#[문제14] 숫자를 입력값으로 받습니다. 
#         만약 숫자가 이외의 값이 들어 오면 "숫자 이외의 문자가 포함되어 있습니다." 아니면 숫자 출력하세요.

num = str(input('숫자를 입력해 주세요 : '))

if num.isnumeric() == True:
    print(num)
else:
    print("숫자 이외의 문자가 포함되어 있습니다." )

#리스트 형태의 자료는 인덱스가 다르므로 안된다.
x = [1,2]
y = [2,1]

if x==y:
    print('참')
else:
    print('거짓')
    
# tuple 형태의 자료는 인덱스가 다르면 안된다 거짓!
x = (1,2)
y = (2,1)

if x==y:
    print('참')
else:
    print('거짓')
    
#set 형은 참으로 나온다 
x = {1,2}
y = {2,1}

if x==y:
    print('참')
else:
    print('거짓')
    
"""
■ 반복문, while
    반복해서 문장을 수행한다.

while 조건문:
    수행해야할 문장
    수행해야할 문장
"""
i = 0
while i <= 10:
    print(i)
    i += 1

#[문제15] 1부터 100까지 합을 구하세요. while문을 이용하세요.

i = 0
result = 0

while i <= 100:
    result += i
    i += 1
    print(result)

#[문제16] 1부터 100까지의 3의 배수를 출력, 합을 구하세요. while문을 이용하세요.

##내 방식
i = 0
result = 0

while i <= 100:
    i += 1
    if i%3 == 0:
        result += i
        print(result)

##선생님 방법 (break 설명)
i = 0
result = 0

while i < 100:
    i += 3
    if i > 100:
        break
    else:
        print(i)
        result += i
        
print(result)

#[문제17] 1부터 10까지 홀수값만 출력하세요.

##내 답안
i = 0
while i < 10:
    i += 1
    if i%2 == 1:
        print(i)
   
##선생님 답안 (continue사용법 설명)
a = 0
while a < 10:
    a += 1
    if a%2 ==0:
        continue
    print(a)



#[문제18] 단을 입력값으로 받아서 구구단을 출력하세요.

#내 정답
gugu = int(input('단수를 입력해 주세요 : '))

a = 0
while a < 9:
    a += 1
    print(str(gugu)+"*"+str(a)+"="+str(a * gugu))
    
    
# 선생님
dan = int(input('단을 입력하세요 : '))
i = 1
while i < 10:
    print('{}*{} = {}'.format(dan,i,dan*i))
    i+=1
    
    
#[문제19] 구구단을 생성하세요

#내꺼
i = 1
j = 1
while i < 10:
    print("="*5 +str(i)+"단"+"="*5 )
    while j < 10:
        print(" {}*{}={}".format(i,j,i*j))
        j += 1
    j = 1
    i += 1
    
#선생님꺼
v_num = 2
while v_num <= 9:
    count = 1
    p_num = 0
    print("{a} {b} 단 {c} ".format(a = "*" *2, b=v_num , c = '*'*2))
    while count <= 9:
        p_num = v_num * count
        print(v_num , "*", count, "=", p_num)
        count = count + 1
    v_num = v_num +1

#[문제20] 반복횟수를 입력해서 화면처럼 출력하세요.
       
    
#내꺼
star = int(input('반복횟수를 입력하세요 : '))
a=1
b=star
while a <= star:
    print(" "*b,"★" * a)
    a += 1
    b -= 1


#선생님
a = int(input("반복횟수를 입력하세요 : "))
cnt = 0
while cnt < a:
    cnt = cnt +1
    print(" "*(a-cnt), "★" *cnt)


"""
■ for 문
for 변수 in (리스트, 튜플 문자열):
    반복 수행해야 할 문장
    반복 수행해야 할 문장
"""

x = ['sql','plsql','r','python']

for i in x:
    print(i)


#튜플(tuple)형식의 자료
x = [(1,2),(3,4),(5,6)]

for (a,b) in x:
    print(a+b)


#[문제21] 학생들의 점수가 90,55,63,78,80 점이 있습니다.
#60점 이상이면 합격, 60점 미만이면 불합격 출력해 주세요.

score = [90,55,63,78,80]
for i in score:
    if i >= 60:
        print('합격')
    else:
        print('불합격')
        
#range(시작, 끝-1,증가분)
range(100)
list(range(100))



#[문제22] 1부터 100까지 합을 구하세요.(for 이용)

j = 0
for i in range(1,101):
    j += i 
    print(j)
    
    
    
#[문제23] 1부터 10까지 출력하세요. 단 4, 8은 제외(for 이용)
for i in range(1,11,1):
    if i == 4 or i == 8:
        continue
    else:
        print(i)
    
        
"""
문제24] 화면과 같이 출력하세요.(for 이용)

가로의 숫자를 입력하세요 : 5
세로의 숫자를 입력하세요 : 5
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
★ ★ ★ ★ ★ 
"""

star_row = int(input("가로의 숫자를 입력하세요 : "))
star_col = int(input("세로의 숫자를 입력하세요 : "))

for i in range(star_col):
    print("★ "* star_row)

#[문제25] 구구단을 출력하세요.(for 이용)

for i in range(2,10):
    print("--{}단--".format(i))
    for j in range(1,10):
        print("{}*{}={}".format(i,j,i*j))
        
        
        
        
        
        
        
        
