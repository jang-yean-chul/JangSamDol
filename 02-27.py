#[문제7] 아래와 같은 문자데이터가 있습니다. 
url = 'http://www.python.org'

#1. http:// 제거한 후 url 변수에 넣어 주세요.
url = url.lstrip("http://")

#2. url변수에 있는 문자 데이터에 '.'을 기준으로 분리하세요.
url = url.split(".",)

#3. url변수에 있는 문자데이터를 www.python.org 모양으로 만드세요.
url = ".".join(url)

#4. url변수에 있는 문자데이터를 대문자로 변환하세요.
url = url.upper()

#5. url변수에 있는 문자데이터를 소문자로 변환하세요.
url = url.lower()

url.capitalize()  #첫글자 대문자


#[문제8] 반복문을 사용하지 않고  * 를 가로 100개 출력
print('*' * 100)


#[문제9] 반복문을 사용하지 않고  * 를 세로 10개 출력
print("*\n" * 10)

"""
■ R의 자료형
    - vector : 같은 데이터 타입을 갖는 1차원 배열 구조
    - matrix : 같은 데이터 타입을 갖는 2차원 배열 구조
    - array  : 같은 데이터 타입을 갖는 3차원 배열 구조
    - list   : 서로 다른 데이터 구조를 갖는 vector들을 저장하거나 또다른 list를 저장한다.
    - data.frame : 서로 다른 데이터 타입을 갖는 컬럼으로 이루어진 2차원 배열 구조(table)
■ PYTHON의 자료형    
- list : 서로 다른 데이터 타입을 갖는 1차원 배열 구조
         데이터의 목록을 다루는 자료형 (파이썬에서 가장 많이 사용하는 자료형)


"""



x = [10,20,30]
x
len(x)
type(x)
x[0]

# list 인덱싱
x[0]
x[-1]

# list 슬라이싱
x[0:2]
x[1:]
x[:-1]
x[-1:]

# list 값을 수정
x[0] = 100
x[1:3] = [200,300]
x

# list 변수 끝에 값을 추가
x.append(400)
x

# 기존 list 변수에 다른 list 변수를 이어 붙이는 방법
x1 = [600,700]
x.extend(x1)
x

# 인덱스를 사용하여 특정 위치에 값을 입력하는 방법
x.insert(4,500)
x

# +를 이용해서 list 변수를 결합하는 방법
x2 = [800,900,1000]
x = x + x2
x

# list변수에 있는 값들 중 마지막 값을 제거하는 방법
x.pop()

# 인덱스 번호에 해당하는 값을 제거하는 방법
x.pop(2)
x

#[문제 10] x.pop을 이용해서 다른 리스트 변수에 값을 넣어주세요.

pop = []
pop.append(x.pop()) #다른 리스트에 있는 마지막 변수를 새로운 리스트 변수에 넣는 것.
pop


# del 함수를 사용해서 리스트 인덱스 값을 삭제하는 방법
del x[3] 
x

drink = ['콜라','사이다','오렌지주스','사과주스','콜라','사이다','콜라']
len(drink)
type(drink)
drink.count('콜라')
drink.index('콜라')
drink.index('콜라',1)
drink.index('콜라',5)   # 뒤에있는 숫자가 인덱스 번호 이상이어야 한다. 여기서는 4번에 두번째 콜라가 있으므로 5이상을 적어줘야 한다.
                        # 5번뒤에있는 콜라를 찾는다는 뜻

# 중첩 리스트
x = [1,2,3,['a','b','c'],4,5]
x[2:5]
x[3]
x[3][0]
x[3][1]
x[3][2]
x[3][0:3]
x[3][-1]
x[3][:2]
x[3].append('d')
del x[3][3]

# 중첩 리스트에 값 수정
x[3][0] = x[3][0].upper()
x[3][1] = x[3][1].upper()
x[3][2] = x[3][2].upper()

# 리스트에 값 수정
x[0] = x[0] * 10
x[1] = x[1] * 10
x[2] = x[2] * 10
x[3][0] = x[3][0] * 10

# 변수 초기화
x.clear()
x

# sort : 리스트내의 값을 기준으로 정렬
x = [1,5,3,4,2]
x.sort()

# reverse : 리스트 인덱스 순서를 반대로 뒤집을때 사용
x.sort(reverse = True)


#[문제11] food 변수를 생성하시고 아래 문제를 풀어보세요.

food = [['김밥','라면','오뎅'],['비빔밥','김치찌게'],['자장면','짬뽕']]
food[0]
#['김밥', '라면', '오뎅']
food[1]
#['비빔밥', '김치찌게']
food[2]
#['자장면', '짬뽕']

#1. 1번 index에 청국장 추가 하세요
food[1] = food[1]+['청국장']
food[1].append("청국장")
food

#2. 2번 index에 탕수육 추가하세요.
food[2] = food[2]+['탕수육']
food[2].append("탕수육")
food

#3. 0번 index에 있는 오뎅 삭제하세요.
food[0] = food[0]+['오뎅']
food[0].append("오뎅")
food

#4. 0번 index에 튀김, 튀김, 떡복이 한꺼번에 추가하세요
food[0] = food[0]+['튀김','튀김','떡복이']
food

#5. 2번 index에 2번 위치에 유산슬 추가하세요
food[2].insert(2,"유산슬")
food

#6. 튀김 갯수를 세어주세요
food[0].count("튀김")

#7. 0번 index만 정렬해주세요
food[0].sort()
food

#8. 0번 index에 마지막 데이터 삭제하세요
food[0].pop()
food


"""
■ tuple(튜플)
    리스트와 유사하지만 틀린점은 수정,삭제,추가 안된다
    리스트 = [], 튜플 = ()
"""
list1 = []
type(list1)

tuple1 = ()
type(tuple1)

tuple2 = 10,20
type(tuple2)

tuple2 = 10,20
tuple3 = (1,)
tuple4 = (1,2,3,4,5)
tuple5 = ('a','b',('ab','cd'))

tuple5[0]
tuple5[0:]
tuple5[2][1]

a = (1,2,3)
b = (4,5,6)
c = a+b
type(c)

a[0]
a[0] = 10     # tuple형태라 불가능  

del a[0]        # tuple형태라 불가능

a.append(4)     # tuple형태라 불가능

a.index(1)
a.count(1)

a = 1,2,3

type(a)

one, two, three = a         # 들어있는 요소의 갯수와 앞에 명시한 갯수가 맞아야 1:1대응이 된다.
one
two
three

"""
■ dictionary
 key   value
이름 = 홍길동, 전화번호 = 01012341234, 주소 = 서울시
"""
dic = {'name' : '홍길동', 'phone' : '01012341234', 'addr' : '서울시'}
sports = {'축구':'매시','농구':'커리','야구':'박찬호'}
type(dic)
type(sports)

sports['축구']  #key값으로 value값을 확인 할 수 있다.

sports['컬링'] = '김영미'    #key,value값을 입력해서 만들기

sports['컬링'] = ['김은정','김경애','김영미','김선영','김초희']    #key,value값을 입력해서 만들기
sports

sports.keys()
sports.values()
sports.items()

sports['농구']
sports.get('농구')

sports['봅슬레이']              # key값이 없으면 오류가 난다.
sports.get('봅슬레이')         # get을 사용하면 오류가 나지않고 NONE로 나오게 된다.

'컬링' in sports.keys()
'매시' in sports.values()
['김은정','김경애','김영미','김선영','김초희'] in sports.values()

del sports['야구']
sports['축구'] = []
sports['축구'] = '손흥민'

sports.clear()

sports = {'축구':'매시','농구':'커리','야구':'박찬호'}
a = sports.values()
list(a)


#unlist 하는 방법

import collections

def flatten(t):
  """
  Generator flattening the structure
  
  >>> list(flatten([2, [2, (4, 5, [7], [2, [6, 2, 6, [6], 4]], 6)]]))
  [2, 2, 4, 5, 7, 2, 6, 2, 6, 6, 4, 6]
  """
  for x in t:
    if not isinstance(x, collections.Iterable):
      yield x
    else:
      yield from flatten(x)
      
list(flatten([2, [2, (4, 5, [7], [2, [6, 2, 6, [6], 4]], 6)]]))     

"""
■ set type
    list type과 비슷하다.
    index 순서가 없다.
    중복을 허용하지 않는다.
"""

a = {1,1,1,2,3,3,2}
type(a)
b = {2,3,4,5}

# 합집합
a.union(b)
a|b

# 교집합
a.intersection(b)
a&b

# 차집합
a.difference(b)
a-b

b.difference(a)
b-a

1 in a
a[0]        #set type은 이게 불가능하다.(인덱스가 없어서 오류가 난다.)

a.remove(1)     # 집합 변수에 값을 삭제
a.add(1)        # 집합 변수에 값을 입력
a.update([5,6,7])       # 여러개의 값을 입력 할 때 
a

x = []  # list
y = ()  # tuple
z ={}   # dictionary
s = set()   # set

type(x)
type(y)
type(z)
type(s)
