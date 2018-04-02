[문제172] emp1.csv, emp2.csv파일을 읽어서 부서별 총액급여를 구하세요. 단 glob을 이용하지 마세요.
##답안
#glob을 이용한 방법
import os
import glob
import pandas as pd

file = 'C:/python/emp*.csv'
file_list = glob.glob(file)
print(file_list)
emp = pd.DataFrame()
for i in file_list:
    temp = pd.read_csv(i, names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
    print(temp)
    emp = emp.append(temp)

print(emp['sal'].groupby(emp['deptno']).sum())
emp

#수동으로 해결
import pandas as pd

emp = pd.DataFrame()
for i in range(1,3):
    file = 'c:/python/emp{}.csv'.format(i)
    temp = pd.read_csv(file, names = ['empid','name','job','mgr','hire_date','sal','comm','deptno'])
    print(temp)
    emp = emp.append(temp)

print(emp['sal'].groupby(emp['deptno']).sum())


데이터 출처 :https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-national-level-data


[문제173] 2016년도에 태어난 아이들의 정보가 들어 있는 year2016파일을 분석해야 합니다.  총 출생수를 생성해주세요.


countBirths()
[('yob2016', 3637321)]

import pandas as pd
yob2016 = pd.read_csv('c:/python/yob2016.txt',names =['name','sex','cn'] )

def countBirths():
    import pandas as pd
    yob2016 = pd.read_csv('c:/python/yob2016.txt',names =['name','sex','cn'] )
    print([('yob2016', yob2016['cn'].sum())])
    

##선생님 답안
import os
def countBirths():
    ret=[]
    count=0
    file = 'c:/python/yob2016.txt'
    name = os.path.basename('c:/python/yob2016.txt')
    name = name.split('.')[0]
    with open(file,'r') as f:
        data=f.readlines()
        for d in data:
            birth = d.split(',')[2]
            count += int(birth)
    ret.append((name,count))
    return ret



import pandas as pd 
import os

file = 'c:/python/yob2016.txt'
name = os.path.basename(file)
name = name.split('.')[0]

yob = pd.read_csv('c:/python/yob2016.txt', names=['name','gender','birth'])


print(name,yob['birth'].sum())



[문제174] yob2016파일에 있는 데이터를 성별 기준으로 출생수, 총 출생수를 구하세요.

import pandas as pd
yob2016 = pd.read_csv('c:/python/yob2016.txt',names =['name','sex','cn'] )

yob2016.groupby('sex').sum()

##정답
import os
def countBirths():
    ret=[]
    fcount = 0
    mcount = 0
    file = 'c:/python/yob2016.txt'
    name = os.path.basename('c:/python/yob2016.txt')
    name = name.split('.')[0]
    with open(file,'r') as f:
        data=f.readlines()
        for d in data:
            birth = d.split(',')
            if birth[1] == 'F':
                fcount += int(birth[2])
            else:
                mcount += int(birth[2])
        ret.append((name,'F',fcount))
        ret.append((name,'M',mcount))
        ret.append((name,'Total',fcount+mcount))
    return ret

a = countBirths()
for i in a:
    print(i[:])
    

import pandas as pd 
import os

file = 'c:/python/yob2016.txt'
name = os.path.basename(file)
name = name.split('.')[0]

yob = pd.read_csv('c:/python/yob2016.txt', names=['name','gender','birth'])

print(yob.groupby('gender').birth.sum())
print(name,yob['birth'].sum())




 [문제175] 2000 ~ 2016년도 년도별 출생수


2000 3777666
2001 3741011
2002 3735651
2003 3799547
2004 3817903
2005 3841440
2006 3952231
2007 3993206
2008 3925486
2009 3814539
2010 3689517
2011 3650434
2012 3648441
2013 3634744
2014 3692930
2015 3683749
2016 3637321    




import os
import glob
import pandas as pd
from pandas import Series,DataFrame
##전체
def countBirths():
    file = 'c:/python/names/yob*.txt'
    file_list = glob.glob(file)
    for i in file_list:
        name = os.path.basename(i)
        name = name.split('.')[0]
        name = name[3:]
        yob = pd.read_csv(i,names = ['name','sex','cn'])
        print(name, yob['cn'].sum())

##범위지정
def countBirths(x,y):
    for y in range(x,y+1):
        file = 'c:/python/names/yob%d.txt'%y
        name = os.path.basename(file)
        name = name.split('.')[0]
        name = name[3:]
        yob = pd.read_csv(file,names = ['name','sex','cn'])
        print(name, yob['cn'].sum())

countBirths(1950, 2016)

##그래프 그리는 법
def popgraph(y1,y2):    
    pop=[]
    year=[]
    for y in range(y1, y2+1):
        f='c:/python/names/yob'+str(y)+'.txt'
        with open(f, "r") as file:
            line=file.readlines()
            a=0
            for l in line:
                a+=int(l.split(',')[-1])
            pop.append(a)
            year.append(y)
    import matplotlib.pyplot as plt
    return(plt.plot(year, pop))

popgraph(1950, 2016)


##선생님 답안
def countBirths():
    ret=[]
    for y in range(2000,2017):
        count=0
        filename='c:/python/names/yob%d.txt'%y
        with open(filename,'r') as f:
            data=f.readlines()
            for d in data:
                birth = d.split(',')[2]
                count += int(birth)
            ret.append((y,count))
    return ret

result = countBirths()
for year, cn in result:
    print(year,cn)

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

year_cn=[]
all_data = pd.DataFrame()
for y in range(2000,2017):
    filename='c:/python/names/yob%d.txt'%y
    name = os.path.basename(filename)
    name = name.split('.')[0]
    df = pd.read_csv(filename, names=['name','gender','birth'])
    all_data = all_data.append(df)
    year_cn.append((name[3:],all_data['birth'].sum()))
    print(name[3:],all_data['birth'].sum())

[문제176]  2000 ~ 2016년도 년도별 출생수 결과를 year.txt 파일에 저장하세요.

def countBirths(x,y):
    file_write = open("c:/python/year.txt",'w')
    for y in range(x,y+1):
        file = 'c:/python/names/yob%d.txt'%y
        name = os.path.basename(file)
        name = name.split('.')[0]
        name = name[3:]
        yob = pd.read_csv(file,names = ['name','sex','cn'])
        a = name+" : "+str(yob['cn'].sum())+"\n"
        print(a)
        file_write.write(a)
    file_write.close()
countBirths(1950, 2016)


##답답
def countBirths():
    ret=[]
    for y in range(2000,2017):
        count=0
        filename='c:/python/names/yob%d.txt'%y
        with open(filename,'r') as f:
            data=f.readlines()
            for d in data:
                birth = d.split(',')[2]
                count += int(birth)
            ret.append((y,count))
    return ret

result = countBirths()
for year, cn in result:
    print(year,cn)

with open('c:/python/year.txt','w') as f:
    for year, birth in result:
        data = '%s,%s\n'%(year,birth)
        print(data)
        f.write(data)

import os
import glob
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

year_cn=[]
all_data = pd.DataFrame()
for f in glob.glob('c:/python/names/yob*.txt'):
    name = os.path.basename(f)
    name = name.split('.')[0]
    df = pd.read_csv(f, names=['name','gender','birth'])
    all_data = all_data.append(df)
    
    year_cn.append((name[3:],all_data['birth'].sum()))
    print(name[3:],all_data['birth'].sum())

with open('c:/python/year_1.txt','w') as f:
    for year, birth in year_cn:
        data = '%s,%s\n'%(year,birth)
        print(data)
        f.write(data)

import os
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import csv

with open('c:/python/total_year.csv','w') as f:
    writer = csv.writer(f, delimiter=',')   # ,를 구분자로 csv를 만들고 싶은 것
    for y in range(2000,2017):
        filename='c:/python/yob%d.txt'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        writer.writerow([name[3:],df['birth'].sum()])
      
[문제177] 2016년도에 태어난 아이 이름 상위 10까지 보여주세요. 성별 상위 5까지 보여주세요.

def top10(x):
     file = 'c:/python/names/yob%d.txt'%x
     name = os.path.basename(file)
     name = name.split('.')[0]
     name = name[3:]
     yob = pd.read_csv(file,names = ["name","sex","cn"])
     yob = yob.sort_values("cn",ascending = False)
     return yob[:10]

top10(2016)
    
def top10(x):
     file = 'c:/python/names/yob%d.txt'%x
     name = os.path.basename(file)
     name = name.split('.')[0]
     name = name[3:]
     yob = pd.read_csv(file,names = ["name","sex","cn"])
     data = yob.sort_values("cn",ascending = False)
     print(data[data["sex"]=='F'][:5])
     print(data[data["sex"]=='M'][:5])

top10(2016)
    
def top(year,sex,num):   #year = 연도 4자리 입력, sex = M,F,ALL입력, num = 보고싶은 순위 입력 
     file = 'c:/python/names/yob%d.txt'%year
     name = os.path.basename(file)
     name = name.split('.')[0]
     name = name[3:]
     yob = pd.read_csv(file,names = ["name","sex","cn"])
     data = yob.sort_values("cn",ascending = False)
     if sex == 'M':
         print(data[data["sex"]=='M'][:num])
     elif sex == 'F':
         print(data[data["sex"]=='F'][:num])
     elif sex == 'ALL':
         print(data[:num])

top(2016,'ALL',10)


##쌤쌤
import pandas as pd 
yob2016 = pd.read_csv('c:\yob\yob2016.txt', names=['name','gender','birth'])


def top(df, n=5, column='birth'):
    return df.sort_values(by=column, ascending=False)[:n]

print(top(yob2016 , n=10))

print(yob2016.groupby('gender').apply(top))





