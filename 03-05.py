
#[문제26] 여러 값을 동일한 변수에 순차적으로 저장할수 있는 용도의 변수 타입과 부호는 ?
#list, []

#[문제27] x 리스트 변수에 1, 3, 5, 7, 9 를 입력하세요
x = ([1,3,5,7,9])  

#[문제28] x 변수에 타입을 확인하세요.
type(x)

#[문제29] x변수에 첫번째값을 확인해주세요
x[0]

#[문제30] x변수에 제일뒤에 값을 확인해주세요
x[-1] 

#[문제31] x변수에 10를 제일 뒤에 추가해주세요.
x.insert(len(x),10)
#2  x.append(10)

#[문제32] x변수에 있는 값들중에 10을 삭제해주세요
del x[x.index(10)]
#2  x.pop(x.index(10))
#3  x.remove(10)

#[문제33] x변수에 1번색인위치에 2를 입력하세요.
x.insert(1,2)

#[문제34] x변수에 1번색인값을 제거해주세요.
x.pop(1)
#2   del x[1]

#[문제35] x 변수에 첫번째 부터  세번째까지 값을 출력해주세요.
print(x[0:3])  #인덱스번호 전까지 출력이 되므로 3을 입력해야 세번째 값까지 출력됨

#[문제36] x 변수에 제일뒤에서 두개 값을 출력해주세요.
print(x[-3:-1])

#[문제37] x 변수를 y변수에 대입한 후 y변수에 11을 추가한 후 x값도 확인 한 후 분석해주세요.
y=x
y.append(11)
y
x    #자동으로 x변수에 y변수의 변화가 적용됨.
id(x)
id(y)

#[문제38] x변수를 z변수에 복사하지만 고유한 변수로 생성해주시고 z변수에 13을 추가 해주세요.
z = list(x)         #고유한 변수로 생성.
z = x[:]  #이렇게 해도 영향을 주지않는 고유한 변수가 생성된다.

import copy   #copy변수 임폴트 해오고
c = copy.deepcopy(x)    #이렇게 하면 독립된 변수를 생성한다.
c
id(x)
id(c)

z.append(13)
z
x

#plsql "package" 한 번 다시 공부하자.

#[문제39] y변수에 값을 x 변수에 넣어주세요.
x = [1,2,3]
y = [4,5,6]

x.extend(y)
x

#[문제40] x 변수에 1번 인덱스의 값을 제거해주세요.
del x[1]

#[문제41] x변수에 1번 부터 3번 인덱스를 제거해주세요.
del x[1:4]  

#[문제42] 중첩리스트를 이용할때 첫번째 항목의 첫번째 항목의 값을 추출해주세요.
x.insert(1,[1,2,3])
x[1][1] 

#[문제43] 리스트형과 비슷하지만 요소의 값을 변경 할 수 없는 타입과 부호는 ?
#tuple, ()
    
#[문제44] 키, 값을 저장하는 데이터 타입과 부호는 ?
#dic (dictionary), {}
    
#[문제45]  아래와 같은 내용을 변수에 입력해주세요. 변수이름은 dict

#           이름 : '홍길동'
#          나이 : 30
#          직업 : '파이썬개발자'
dict = {'이름' : '홍길동', '나이' : 30, '직업' : '파이썬개발자'}          
  
#[문제46] dict변수 키를 출력하세요.
dict.keys()

#[문제47] dict변수 값을 출력하세요.
dict.values()

#[문제48] dict변수의 키, 값을 출력해주세요.
dict 

#[문제49] dict변수의 이름만 출력해주세요.
dict['이름']

#[문제50] dict변수의 주소 = '서울' 추가해주세요
#'주소' in dict.keys()
#'서울' in dict.values()   #in 은 있나없나를 확인하는 것.
dict['주소'] = '서울'   #이렇게 삽입 할 수 있다.

#[문제51]  dict변수의 나이값을 32 수정하세요.
dict["나이"] = 32


#[문제52] 구구단을 만드세요. 2단에서 9단까지만 입력하세요, [0은 구구단 전부를 출력합니다.]: 
gugu = int(input("단수를 입력하세요 : "))
if gugu == 0:
    for i in range(2,10):
        print("---{}단---".format(i))
        for j in range(2,10):
            print("{}*{} = {}".format(i,j,i*j))
elif 2<= gugu <=9:
    print("---{}단---".format(gugu))
    for j in range(2,10):
        print("{}*{} = {}".format(gugu,j,gugu*j))
else:
    print("2단에서 9단까지만 입력해주세요.(0입력시 2~9단 출력됩니다.)")




#[문제53]lst 변수에 a,b,c,d값이 있습니다. for문을 이용하여 아래화면과 같이 출력하세요.

lst = ['a','b','c','d']
lst

for i in lst:
    print("{}번 {}값이 있습니다.".format(lst.index(i),i))
    
for i in range(len(lst)):
    print("{}번 {}값이 있습니다.".format(i, lst[i]))

for i, name in enumerate(lst):      #enumerate는 인덱스번호와 값을 return해준다.
    print("{}번 {}값이 있습니다.".format(i,name))
    
0번 a값이 있습니다.
1번 b값이 있습니다.
2번 c값이 있습니다.
3번 d값이 있습니다.


[문제54] 1부터 9까지 x 리스트 변수에 넣어주시고 y변수는 x 변수의 값을 2곱한 값으로 넣어 주세요
x = [1,2,3,4,5,6,7,8,9]
x = range(1,10)
y = []
for i in range(len(x)):
    y.append(x[i]*2)

for i in x:
    y.append(i*2)
y

# 리스트 내포 (list compregension), 리스트 내장객체
# [표현식 for 항목 in 반복가능한 객체]
y = [i*2 for i in x]


[문제 55] apple, banana, orange 리스트 변수에 값을 입력하시고 이 값들의 길이를 출력해주세요
fruit = ['apple','banana','orange']
for i in fruit:
    print(len(i))
    
[len(i) for i in fruit]

[문제 56]변수에 값이 들어 있습니다.
lst1 = [1,2,3]
lst2 = [4,5,6]

[4,5,6,8,10,12,12,15,18]

lst1
x = []
for i in lst1:
    for j in lst2:
        x.append(i * j)

[i * j for i in lst1 for j in lst2]


[문제57]  1부터 100까지 값중에 짝수만 x 변수에 넣어 주세요.
lst = range(1,101)

x = []
for i in lst:
    if i % 2 ==0:
        x.append(i)

x = [i for i in range(1,101,1) if i%2 == 0]
x



[표현식 for 항목변수 in  반복 가능한 객체]

<for문 sub for문>
[표현식 for 항목변수 in  반복 가능한 객체
        for 항목변수 in  반복 가능한 객체
        .........
        for 항목변수 in  반복 가능한 객체]

<for문 if문>
[표현식 for 항목변수 in  반복 가능한 객체 if 조건 1
        for 항목변수 in  반복 가능한 객체 if 조건 2
        ....
        for 항목변수 in  반복 가능한 객체 if 조건 n]

[문제58] 튜플변수에 사과, 귤, 오렌지, 배, 포도, 바나나, 자몽, 키위, 딸기, 블루베리, 망고를 입력하시고 
과일이름중에 세글자 이상인 과일 fruit_lst변수에 입력해주세요.

fruit = ('사과','귤','오렌지','배','포도','바나나','자몽','키위','딸기','블루베리','망고')

fruit_lst = []
for i in range(0,len(fruit)):
    if len(fruit[i]) >= 3:
        fruit_lst.append(fruit[i])
        
fruit_lst = [i for i in fruit if len(i) >= 3]


[문제59] 딕셔너리 변수에 값이 들어 있습니다. 과일이름을 대문자로 출력해주세요.
dict = {100:"apple",200:"banana",300:"orange"}

for i in dict.values():
    print(i.upper())

[i.upper() for i in dict.values()]


■ 함수 
    반복되는 코드를 하나로 묶어서 처리하는 방법
    기능의 프로그램

def 함수이름(인수,인수....):
    수행할 문장1
    수행할 문장2
    .....
    수행할 문장n

함수이름()   #함수호출 방법

프로시저와 함수의 차이점?

def message():
    print("오늘 하루도 행복하자")

message()

def message():
    print("오늘 하루도 행복하자")
    return "happy"

word = message()
print(word)

[문제 60] 함수에 두개의 숫자를 인수값으로 받아서 값을 비교하는 프로그램을 작성하세요.

def van(x,y):
    if x > y:
        print("{}이 {}보다 큽니다".format(x,y))
    elif x == y:
        print("값이 같습니다".format(x,y))
    else:
        print("{}이 {}보다 큽니다".format(y,x))
        

[문제 61]두 인수값을 받아서 합한 값을 리턴해주는 함수를 작성하세요.
def krkr(x,y):
    return x+y
krkr(10,500)


# 인수값이 여러개일 경우
def 함수이름(*인수):
    수행할 문장

sum(10,2,3,4,5)
sum(10,20,40,60,80,100)

def sum(*arg):   #   *arg  = 인수의 갯수가 가변적이다 라는 뜻 
    total = 0
    for i in arg:
        total = total+i
    return total


[문제 62]
cal("sum",1,2,3,4,5)
cal("multiply",1,2,3,4,5)

def cal(x,*y):
    if x == "sum":
        total = 0
        for i in y:
            total = total+i
    elif x == "multiply":
        total = 1
        for i in y:
            total = total * i
    return total

[문제 63] 여러 숫자를 인수값으로 받아서 합과 평균을 출력하는 aggF함수를 생성하세요.
aggF(1,2,3,4,5,6,7,8,9,10)

합 : 55
평균 : 

   
def aggF(*x):
    total = 0
    for i in x:
        total = total+i
    print("합 : ",total)
    print("평균 : ",total/len(x))
    
#표준편차 : 값의 분산의 정도를 알기위해서 사용
    # 평균에 루트를 씌워서 표현

def f1(a,b):
    return a+b
    return a-b

f1(1,2)  # 하나밖에 안된다

def f1(a,b):
    return a+b,a-b
f1(1,2)   # tuple형식으로 2개의 값이 전부 출력된다.


def f2(arg):
    if arg ==0:
        return      #에러없이 그냥 실행하려면 아무것도 안쓰고 return처리!
    print(arg,"값입니다.")

f2(0)
f2(2)


def f3(name,age,gender = "M"):   # 기본값을 M으로 하겠다는 것, 그리고 기본값을 넣으려는 함수는 무조건 뒤에
    print("이름은 ",name)
    print("나이는 ",age)
    if gender == "M":
        print("남자")
    else:
        print("여자")
        
f3("홍길동",30)   #3번째 인수에 아무것도 입력하지 않으면 자동으로 M이 입력된다.
f3("김영미",20,"F")


x = 10 #전역변수(global), 변수는 프로그램이 종료될때까지 어디서든지 사용
def f4(x):
    print('x변수 값은', x)
    x=20 #지역변수, 로컬변수, 함수안에서만 사용한다.
    print('x변수 값은', x)

f4(x)
print(x)

def f4():
    global x
    x=20 #지역변수, 로컬변수, 함수안에서만 사용한다.
    print('x변수 값은', x)

f4()
print(x)
