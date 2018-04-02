import numpy as np
import pandas as pd
import matplotlib as mpl   #그래프 그리는 패키지
import matplotlib.pyplot as plt   #그래프 그리는 패키지
from matplotlib import font_manager,rc  #font관리, 한글 나오게 설정
font_name = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf").get_name() #font관리, 한글 나오게 설정
rc('font',family = font_name) #font관리, 한글 나오게 설정
%matplotlib inline

plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1])
plt.show()

x = np.arange(0,23,0.01) #0~23까지 0.01간격으로 데이터 생성
y = np.sin(x)

plt.figure(figsize=(10,8))  #figsize가 들어가야 작동한다
plt.plot(x,y)
plt.show()

plt.figure(figsize=(12,8))  # 그래프 사이즈, figsize가 들어가야 작동한다
plt.plot(x,y)
plt.grid()  #배경에 분할 사각형 추가
plt.xlabel('시간')    # x레이블
plt.ylabel('진폭')    # y레이블
plt.title('sinewave')   # 차트 제목
plt.show()

x = [1,2,3,4,5,6,7,8,9]
plt.plot(x, color = "red", linestyle = "dashed", marker = "o", markerfacecolor = "yellow", markersize = 5)

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([9,8,7,9,8,3,2,4,3,4])
plt.scatter(x,y)    #산점도
plt.scatter(x,y,marker = '>')    #산점도, 점모양을 둥근거에서 뾰족한걸로

colormap = x
plt.scatter(x,y,s=50,c = colormap,marker = ">")
plt.colorbar()

from pandas import Series, DataFrame
data = {"홍길동":[15,13,11],"윤건":[13,14,15], "나얼":[10,9,12]}
df = DataFrame(data,index = [2015,2016,2017])
df
df[df.index == '2015'].max()
df.rank()   #액시스해서 축을 변경해서 할 수 있다.

ad = df.rank()
plt.plot(ad)
ad
plt.plot(ad.ix[:,0],label = "나얼",linestyle = "-.",color = "r")
plt.plot(ad.ix[:,1],label = "윤건",linestyle = "--",color = "b")
plt.plot(ad.ix[:,2],label = "홍길동",linestyle = ":",color = "y")
plt.title("기록 순위 비교 그래프",fontsize = 15)
plt.xlabel("연도",fontsize = 10)
plt.ylabel("순위",fontsize = 10)
plt.xlim([2014.9,2017.1])
plt.ylim([0.9,3])
plt.xticks([2015,2016,2017],['2015년','2016년','2017년'])
plt.yticks([1,2,3])
plt.legend(loc = 1) # 1~10


df.plot(kind = "bar") #막대그래프

df.plot(kind = "barh") #수평 막대그래프

df.plot(kind = "barh",stacked = True)

df.plot(kind = "bar", stacked = True, legend = False)

df.rank(axis = 0)
df.rank(axis = 1)

[문제178] yob2016.txt 데이터셋을 이용해서 상위 5위 까지 여자 아기 이름 출생수를 막대그래프로 그리세요.

##내꺼
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

yob2016 = pd.read_csv('c:/python/yob2016.txt',names =['name','sex','cn'])

top5 = yob2016[yob2016["sex"] == 'F'].sort_values('cn',ascending=False)[:5]
top5 = top5.set_index(top5['name'])

top5.plot(kind = "bar",color = "g")
plt.title("2016년 여아 이름 수 top5",fontsize = 15)
plt.xlabel("여아 이름",fontsize = 10)
plt.ylabel("출생 수",fontsize = 10)
plt.ylim([10000,21000])


##쌤꺼!
def top(df,n = 5, column = 'cn'):
    return df.sort_values(by = column, ascending = False)[:n]

data = yob2016.groupby('sex').apply(top)

fdata = data.loc['F'][['name','cn']]

fdata.plot(kind = 'bar')

fdata = fdata.set_index(fdata['name'])

fdata.plot(kind = 'bar',color = 'y')


file = "c:/python/stats_104102.xlsx"
#첫번째에 제목, 두번째에 연도가 들어있다.(엑셀은 두번째 줄이 컬럼명이다. 만약 첫번째줄을 컬럼명으로하고싶으면 헤더를 0으로 놓으면된다.)
sheet_name = "stats_104102"

data = pd.read_excel(file, sheet_name, header = 1)
data
data.index
data.columns
data.values
data.plot(kind = "bar")

data.ix[['서울','경기']].plot(kind = "bar")
data.loc[['서울','경기','부산']].plot(kind = "barh")


[문제179] 2010 ~ 2016  년도까지 성별 출생 현황을 그래프를 그리세요.

import os
import glob
import pandas as pd
from pandas import Series,DataFrame


def countBirths(x1,x2):
    a = DataFrame()
    for y in range(x1,x2+1):
        file = 'c:/python/names/yob%d.txt'%y
        name = os.path.basename(file)
        name = name.split('.')[0]
        name = name[3:]
        yob = pd.read_csv(file,names = ["name","sex","cn"])
        data = yob.sort_values("cn",ascending = False)
        data1 = {'F':[data["cn"][data["sex"]=='F'].sum()],'M':[data["cn"][data["sex"]=='M'].sum()]}
        df = DataFrame(data1,index = [name])
        a = a.append(df)
    plt.plot(a["F"],linestyle = "--",color = "b")
    plt.plot(a["M"],linestyle = ":",color = "r")
    plt.legend()
    plt.xlabel("년도",fontsize = 10)
    plt.ylabel("출생 수",fontsize = 10)

countBirths(2000, 2016)      


##선생님 답안
import csv
import os
from pandas import Series,DataFrame
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
%matplotlib inline

with open('c:/python/year_gender_total.csv','w') as f:
    writer = csv.writer(f, delimiter=',')
    for y in range(2000,2017):
        filename='c:/python/names/yob%d.txt'%y
        name = os.path.basename(filename)
        name = name.split('.')[0]
        df = pd.read_csv(filename, names=['name','gender','birth'])
        gender_cn = df['birth'].groupby(df['gender']).sum()
        f_cn = str(gender_cn.loc['F'])
        m_cn = str(gender_cn.loc['M'])
        writer.writerow([name[3:],f_cn, m_cn])
      
df = pd.read_csv("c:/python/year_gender_total.csv", names=['년도','여자','남자'])

df = df.set_index("년도")

df.ix[:,0]

df.plot()
df.plot(kind="bar")
df.plot(kind="barh")

plt.plot(df.ix[:,0], label="여자", color="r", linestyle="--")
plt.plot(df.ix[:,1], label="남자", color="b", linestyle=":")
plt.title("성별 출생 현황", fontsize=15)
plt.xlabel("년도",fontsize=10)
plt.ylabel("출생수",fontsize=10)
plt.legend()
plt.grid()
plt.annotate("최고", 
             xy=(df[df['여자'] == df['여자'].max()].index.values, df['여자'].max()),
             xytext=(-90, -50),
             textcoords='offset points', 
             fontsize=10, arrowprops=dict(arrowstyle="->"))
plt.annotate("최고", 
             xy=(df[df['남자'] == df['남자'].max()].index.values, df['남자'].max()),
             xytext=(-90, -50),
             textcoords='offset points', 
             fontsize=10, arrowprops=dict(arrowstyle="->"))

"""
If you are using conda, you can install from the conda-forge channel:
conda install -c conda-forge wordcloud

If you don't use conda, you can install via pip, but that will require having a C compiler set up:
pip install wordcloud
"""

from wordcloud import WordCloud, STOPWORDS  #불용어
import matplotlib.pyplot as plt

with open('c:/python/문재인대통령취임사.txt','r') as file:
    text = file.read()

text

wordcloud = WordCloud(font_path = "c:/Windows/Fonts/malgunbd.ttf",stopwords = STOPWORDS,
                      background_color = "white",width = 1000,height = 800).generate(text)
#워드클라우두으으으으으
plt.figure(figsize = (10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

from scipy.misc import imread

heart_mask = imread("c:/python/heart.jpg",flatten = True)

wordcloud = WordCloud(font_path = "c:/Windows/Fonts/malgunbd.ttf",stopwords = STOPWORDS,
                      background_color = "white",width = 1000,height = 800,mask = heart_mask).generate(text)

plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation="gaussian")
plt.axis("off")
plt.show()






