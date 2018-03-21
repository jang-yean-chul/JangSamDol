import pandas as pd
from pandas import Series,DataFrame

student = DataFrame([[60,80,70],[50,75,85],[90,80,85]],index = ['홍길동','박찬호','손흥민'], columns = ['영어','수학','국어'])

student

student = student.set_value('제임스','영어','100')
student = student.set_value('제임스','수학','50')
student = student.set_value('제임스','국어','80')

student.ix['제임스','영어'] = 98
student.loc['제임스','영어']

student = student.set_value('제임스','영어','90')

student_new = DataFrame([[60,80,70],[50,75,85],[90,80,85]],index = ['윤건','김건모','이문세'], columns = ['영어','수학','국어'])

student = student.append(student_new)


student1 = DataFrame([[60,80,70],[50,75,85],[90,80,85]],index = ['싸이','나얼','윤상'], columns = ['영어','수학','국어'])

student = pd.concat([student,student1])     #두 개의 데이터프레임 이어 붙이기

student['과학'] = [100,80,86,90,95,90,80,70,90,70]

student['한국사'] = '조선'   #컬럼명 한국사로 모든행에 조선이들어감
del student['한국사']  #한국사 컬럼 삭제

student = student.drop('제임스')     #제임스row삭제
student['영어']
student[['영어','국어']]
student.ix['나얼']
student.ix[7]
student.ix[0:5]     #index번호를 사용할때는 ix를 붙여서

student.ix['나얼',['영어','국어']]
student.ix[['나얼','윤건'],['영어','국어']]
student.ix[['나얼','윤건'],[0,2]]
student.ix[[3,7],[0,2]]
student.ix[:'윤건']
student.loc['윤건']
student[student.index.isin(['나얼','윤건'])]

student[(student['수학']> 75) & (student['과학'] > 80)]

student[(student['수학']> 75) | (student['과학'] > 80)]

student.loc[student['수학'] > 90]

student.loc[student['국어'] == 85]

student.loc[student['수학'].isin([75,95])]

student.ix[student['과학'] <= 80]

student.ix[student['과학'] <= 80,'과학']

student.ix[student['과학'] <= 80,['수학','과학']]

student.ix[student['과학'] <= 80,:'국어']

student.ix['윤건']
student.xs('윤건')
student.xs('영어',axis=1)
student['영어']

student.rename(index = {'윤상':'김상'})
student = student.rename(columns = {'과학':'물리'})

obj1 = Series([10,5,3,7],index = ['a','b','c','d'])
obj2 = Series([2,4,6,8,10],index = ['a','b','c','e','f'])

##연산작업
obj1 + obj2
obj1.add(obj2,fill_value = 0)
obj1 - obj2
obj1.sub(obj2,fill_value = 0)
obj1 * obj2
obj1.mul(obj2,fill_value = 0)
obj1 / obj2
obj1.div(obj2,fill_value = 0)

obj1*10


import numpy as np
df1 = DataFrame(np.arange(6).reshape(2,3),index = ['2015','2016'],columns = ['python','sql','plsql'])

df2 = DataFrame(np.arange(12).reshape(3,4),index = ['2014','2015','2016'],columns = ['python','r','sql','plsql'])

df1 + df2
df1.add(df2,fill_value = 0)
df1.sub(df2,fill_value = 0)
df1.mul(df2,fill_value = 1)
df1.div(df2,fill_value = 1)

obj = np.arange(15).reshape(5,3)

obj1 = obj[0]

obj1 + obj

# broadcastion(브로드캐스팅)
obj + obj1

obj1.repeat(5)
obj1.repeat(5).reshape(3,5)
obj1.repeat(5).reshape(3,5).T
obj - obj1.repeat(5).reshape(3,5).T

df1 = DataFrame(np.arange(15).reshape(5,3),index= [str(i) for i in range(2012,2017)],columns = ['서울','부산','광주'])

df1.ix[0]

type(df1)
s = df1.ix[0]
type(s)

#모양이 달라도 브로드캐스트가 돌아가서 연산작업이 가능하다.
df1 + s
2000

s2 = Series([1,2,3,4],index = ['서울','부산','광주','제주'])

df1 + s2    #연산작업이 가능하지만 없는 컬럼에 대해서는 NAN값으로 나온다.

df1 = DataFrame(np.arange(15).reshape(5,3),index= [str(i) for i in range(2012,2017)],columns = ['서울','부산','광주'])
df1
s3 = Series([0,3,6,9,12],index = [str(i) for i in range(2012,2017)])
s3

df1 + s3
df1.add(s3,axis = 0)    #0: row  1: column  *index값이 일치해야 한다.


[문제112] 아래와 같은 모양의 표를 생성하세요. 

      PYTHON   R  SQL
2014      60  90   50
2015      80  65   75
2016      70  75   85

from pandas import Series,DataFrame

df1 = DataFrame([[60,90,50],[80,65,75],[70,75,85]], index = [str(i) for i in range(2014,2017)], columns = ['PYTHON','R','SQL'])
df1

[문제113] 'PYTHON' 열을 선택하세요

df1['PYTHON']

[문제114] '2014' 행 정보를 출력하세요.

df1.loc['2014']

[문제115] 인덱스번호를 기준으로 1부터 2번까지 출력하세요.

df1.loc[1:3]

[문제116] PYTHON의 값을 기준으로 60보다 큰값을 가지고 있는 행 정보를 출력하세요.

df1[df1['PYTHON'] > 60]

[문제117] PYTHON의 값을 기준으로 60 보다 큰값을 가지고 있는 PYTHON 정보만 출력하세요.

df1[df1['PYTHON'] > 60]['PYTHON']

[문제118] '2015' 행값 중에 PYTHON 정보만 출력하세요

df1.loc['2015']['PYTHON']

[문제119] '2015'  행값 중에 PYTHON, R 정보 출력하세요 

df1.loc['2015'][['PYTHON','R']]

[문제120] 'R' 열 정보를 출력하세요.

df1['R']

[문제121] 2013 행을 추가하세요. PYTHON : 70,  SQL : 90, R : 85

df2 = DataFrame([[70,90,85]], index = [str(2013)], columns = ['PYTHON','R','SQL'])
df1 = df2.append(df1)

df1.at['2013','PYTHON'] = 70  #  데이터프레임[행,열] = 수정값
df1 = df1.drop('2013')   #행지우기

[문제122] PLSQL 열을 추가한 후 값은 0로 설정하세요

df1['PLSQL'] = 0
df1

[문제123] PLSQL 열의 값은 2013 : 50, 2014 : 60, 2015 : 80, 2016 : 90 으로 수정하세요.

df1['PLSQL'] = [50,60,80,90]
df1

[문제124] 2016년도에 있는 정보 출력하세요

df1.loc['2016']


[문제125] 2015, 2016년도에  정보 출력하세요.

df1.loc[['2015','2016']]

[문제126] 2016년도에 PYTHON 정보만 출력하세요.

df1.loc['2016']['PYTHON']

[문제127] 2016년도에 PYTHON, SQL 정보 출력하세요

df1.loc['2016'][['PYTHON','SQL']]

[문제128] SQL 점수가 80점보다 이상인 정보를 출력하세요.

df1[df1['SQL']>=80]

[문제129]PYTHON 점수가 80 이상 또는 SQL 점수가 90 이상인 데이터 출력하세요.

df1[(df1['PYTHON'] >= 80) | (df1['SQL'] >=90)]

[문제130] PYTHON 점수가 80 이상 이고 SQL 점수 90 이상인 데이터 출력하세요.

df1[(df1['PYTHON'] >= 80) & (df1['SQL'] >=90)]

[문제131] SQL 점수가 80점 미만인 SQL정보 출력하세요

df1[df1['SQL'] < 80]['SQL']




df1.add(s3,axis = 0)   #0 : row,   1:column

obj = Series([2,3,5,6],index = ['d','c','b','a'])

# Series에서 인덱스번호를 기준으로 정렬하는 방법
obj.sort_index()
obj.sort_index(ascending = False)

# Series에서 값을 기준으로 정렬하는 방법
obj.sort_values())
obj.sort_values(ascending = False)


import numpy as np
df = DataFrame(np.arange(8).reshape(2,4),index = ['two','one'],columns = ['b','d','a','c'])

df.sort_index()
df.sort_index(ascending = False)

df.sort_index(axis= 1)
df.sort_index(ascending=False,axis = 1)

df.sort_values(by = 'b', axis = 0, ascending = False)
df.sort_values(by = 'one', axis = 1, ascending = False)

obj1 = Series([78,88,92,79,67,91,70,86,90,90])
obj1.sort_values()

obj1.rank()
obj1.rank(ascending = False)  #같은 값이 나와서 .5단위로 나온다.
obj1.rank(ascending = False,method='average')  #.5 단위시 그냥 .5
obj1.rank(ascending = False,method='min')  #.5 단위시 낮은값으로
obj1.rank(ascending = False,method='max')  #.5 단위시 높은값으로
obj1.rank(ascending = False,method='first')  #.5 단위시 먼저나온데이터 순위로
obj1.rank(ascending = False,method='dense')  #.5 중복순위를 기재
rank


df = DataFrame({'영어':[60,70,80],'수학':[50,72,86]}, index = ['홍길동','박찬호','손흥민'])
df
df.rank(ascending = False)
df.rank(ascending = False,axis = 1)  #학생들 별로 과목순위를 보고싶으면 axis = 1
df.rank(ascending = False,axis = 0)  #과목순위를 보고싶으면 axis = 0 


