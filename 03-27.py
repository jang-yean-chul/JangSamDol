#크롤링이후 데이터를 별도의 디렉토리에 저장하고 진행하려면?

#파일의 크기 확인

from os.path import getsize

getsize('c:/r/emp.csv')

#디렉토리에 있는 파일 확인

import os
import glob

folder = 'c:/python'
file_list = os.listdir(folder)
file_list

#특정한 파일들의 목록 확인
file = 'c:/python/*.csv'
file_list = glob.glob(file)
file_list

#현재 디렉토리 확인
import os
dir = os.getcwd()
dir

os.chdir('..') #상위 디렉토리로 올라가는 것
os.getcwd()
os.chdir(dir)
os.getcwd()

#디렉토리 생성
import os
from os.path import exists

dir = input("새로 생성할 디렉토리 이름을 입력하세요 : ")

#우리가 원하는 데이터를 검증할수 있는지 볼수있는 문장.
if not exists(dir):
    os.mkdir(dir)
    print('[%s] 디렉토리를 생성했습니다'%dir)
else:
    print('[%s] 디렉토리는 이미 존재합니다.'%dir)

#파일 존재여부 확인
file = 'c:/python/emp1.csv'
if exists(file):
    print('[%s] 파일이 존재 합니다'%file)
else:
    print('[%s] 파일이 없습니다.'%file)


[문제185] 중앙일보에서 인공지능에 기사 검색을 한 후 그 내용을  아래와 같이 저장하세요.

Enter the file name and file location : c:/20180327/중앙일보.txt

from bs4 import BeautifulSoup
import urllib.request as req
import re

url = "http://search.joins.com/JoongangNews?Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews&PeriodType=All&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True"
res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser")

#url링크 따오는 법
a = []
for link in soup.findAll('a',attrs = {'href':re.compile("http://")}):
    a.append(link.get('href'))   
aa = set(a)

#날짜 따오는법
l = soup.findAll('span',{'class':'byline'})
date = []
for i in l:
    text = i.get_text(strip = True)
    text = text[-16:-6]
    date.append(text.replace(".",""))

#디렉토리 생성 여부
os.getcwd()
for i in date:
    dir = i
    if not exists(dir):
        os.mkdir(dir)
        print('[%s] 디렉토리를 생성했습니다'%dir)
    else:
        print('[%s] 디렉토리는 이미 존재합니다.'%dir)  

#기사 끌어오기
content =[]
for i in aa:
    url = i
    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser")
        
    a = soup.find_all('h1',class_="headline mg")
    b = soup.findAll('div',{'id':'article_body'})
    cnt= 0
    for i in a:
        content.append(i.get_text(strip=True) +"\n\n"+ b[cnt].get_text(strip = True))
        cnt += 1

#기사 이어 붙이기
fre = {}
cnt = 0
for i in date:
    if i in fre:
        fre[i] = fre[i]+"\n===============================================================================\n"+content[cnt]
        cnt += 1
    else:
        fre[i] = content[cnt]
        cnt += 1
        
#파일 생성하기
for i in fre.keys():
    f = open("c:/%s/중앙일보.txt"%i,'w',encoding = 'UTF-8')
    f.write(fre[i])
    f.close()


######################################################################
##쌤꺼
import urllib.request
from bs4 import BeautifulSoup
import os
from os.path import exists

def get_save_path():
    save_path = input("Enter the file name and file location : " )
    save_path = save_path.replace("\\", "/")
    if not exists(os.path.split(save_path)[0]):
        os.mkdir(os.path.split(save_path)[0])
    return save_path


def fetch_list_url():
    params = []

    for i in range(1,3):
        list_url = " http://search.joins.com/JoongangNews?page=" + str(i) + "&Keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&SortType=New&SearchCategoryType=JoongangNews"
    
        url = urllib.request.Request(list_url)
        res = urllib.request.urlopen(url).read().decode("utf-8")
        soup= BeautifulSoup(res, "html.parser")
        for j in range(0,10):
            soup2 = soup.find_all('div',class_="text")[j]
            soup3 = soup2.find('a')['href']
            params.append(soup3)
    return params


def fetch_list_url2():
    params2 = fetch_list_url()
    f = open(get_save_path(),'w',encoding="utf-8")
    for i in params2:
        list_url2 = i
        url2 = urllib.request.Request(list_url2) 
        res2 = urllib.request.urlopen(url2).read().decode("utf-8")  
        soup = BeautifulSoup(res2, "html.parser")

        result = soup.find_all('div',id="article_body")[0]
        final = result.get_text(strip=True, separator='\n')
        f.write(final+"\n\n")
    f.close()


fetch_list_url2()


##css(cascading stylesheets)

from bs4 import BeautifulSoup

html = """
<html>
<body>
<div id = "lecture1">
<h1> 데이터 과학 </h1>
</div>
<div id = "lecture2">
<h1> 빅데이터 분석 </h1>
<ul class = "subject">
<li> SQL 강좌 </li>
<li> R 강좌 </li>
<li> PYTHON 강좌 </li>
</ul>
</div>
</body>
</html>
"""


soup = BeautifulSoup(html,"html.parser")

soup.find('h1').string
soup.find('h1').get_text()

soup.select_one('div > h1').string
soup.select_one('div#lecture1 > h1').string ##id대신에 '#'으로 표기
soup.select_one('div#lecture2 > h1').string ##id대신에 '#'으로 표기

subject = soup.select('div#lecture2 > ul.subject > li')

for i in subject:
    print(i.string)





url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")

l = soup.select("div.head_info > span.value")
for i in l:
    print(i.string)
    
dollar = soup.select_one("div.head_info > span.value").string
print('USD/KRW',dollar)

soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").string
soup.select_one("#exchangeList > li > a.head.eur > div > span.value").string
soup.select_one("#exchangeList > li > a.head.jpy > div > span.value").string









