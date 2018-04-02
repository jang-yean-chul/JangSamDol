BeautifulSoup

cmd창을 관리자 모드로 실행해서 pip install beautifulsoup4

from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1> 스크래핑 </h1>   
<p> 웹페이지 분석하기 </p>
<p> 데이터 정제작업하기 </p>
</body>
</html>"""
# 헤더부분<h>



# html 분석
soup = BeautifulSoup(html, "html.parser")

# 원하는 태그내용 가지고 오기
h1 = soup.html.body.h1   #soup 안에 html 안에 body안에 h1
h1.string

p1 = soup.html.body.p
p1.string

p1.next_sibling
p1.next_sibling.next_sibling  #sql 에서 sibling 계층검색

p2 = p1.next_sibling.next_sibling
p2.string


html = """
<html>
<body>
<h1 id = 'title'> beautifulsoup </h1>   
<p id = 'subtitle'> 스크레핑 </p>
<p> 데이터 추출하기 </p>
</body>
</html>"""

soup = BeautifulSoup(html, "html.parser")

soup.find(id = 'title').string

title = soup.find(id = 'title')
title.string

soup.find(id = 'subtitle').string

soup.find(h1).string # 안된다
soup.find(p).string # 안된다

soup.find('title').string # 안된다



html = """
<html>
<body>
<ul>
<li> <a href = "http://www.itwill.com"> 아이티윌 </a></li>
<li> <a href = "http://www.naver.com"> 네이버 </a></li>
</ul>
</body>
</html>"""

soup = BeautifulSoup(html,"html.parser")
a1 = soup.html.body.ul.li.a
a1.string

link = soup.find_all('a') #a라는 속성에 대해서 다 찾아보기

for i in link:
    print(i.attrs['href'])
    print(i.string)

with open ("c:/python/a.html",encoding = 'UTF8') as html:
    soup = BeautifulSoup(html, "html.parser")

soup.prettify
soup.find('title').string
soup.find('body')
soup.find('p').string
soup.findAll('p') #find_all이나  findAll이나 똑같다.

l = soup.findAll('p')
for i in l:
    print(i.get_text())  #text가 깔끔하게 나온다.

soup.find('body').get_text()
soup.find('body').get_text(strip = True)  # \n을 지우는 방법

l = soup.find('body')
for i in l:
    print(i)  # findAll이 아닌 find를 사용 할떄는 i.get_text()를 쓰게 되면 오류가 발생한다.

l = soup.findAll('body')
for i in l:
    print(i.get_text())  #text가 깔끔하게 나온다.

soup.find('a')
l = soup.findAll('a')

#url말고 텍스트만 보고싶으면 변수에 담고 반복문
for i in l: 
    print(i.get_text())


soup.findAll('a',{'class' : 'cafe1'})  #class값 추가해서 찾아내기

l = soup.findAll('a',{'class' : 'cafe3'})  #class값 추가해서 찾아내기
for i in l:
    print(i.get_text())

l = soup.findAll('',{'class' : 'cafe1'})  # 속성안에 모든값중에서 찾아내겠다라는 뜻으로 a(속성값)를 안써도 된다.
for i in l:                             # 즉, class가 cafe1인 값을 찾아내겠다는 것.
    print(i.get_text())


l = soup.findAll('a',{'id' : 'link1'})  
for i in l:
    print(i.get_text())

soup.findAll(class_='cafe1')

for link in soup.findAll('a'): #link만 따오는 법
    print(link.get('href'))

soup.find(['a','p'])
soup.findAll(['a','p'])

l = soup.findAll(['a','p'])
for i in l:
    print(i.get_text())

soup.findAll(text = '환영합니다.')

import re  #문자열을 찾아보고싶을떄 사용하는 함수
soup.findAll(text = re.compile('환영'))

soup.findAll('p')
soup.findAll('p',limit = 2)


with open ("c:/python/a.html",encoding = 'UTF8') as html:
    soup = BeautifulSoup(html, "html.parser")

for link in soup.findAll('a',attrs = {'href':re.compile("https://")}):
    print(link.get('href'))


from bs4 import BeautifulSoup
import urllib.request as req  # urllib.request 를 req 로 만듬

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp" #주소

res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser")

soup.find("title").string
soup.find("wf").string




[문제 180]이 주소로 접속하셔서 게시글을 출력하세요.

url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser")

soup.prettify #게시글 구조 확인


l = soup.findAll(class_ = 'con') #class = con인 위치에 글있는거 확인

for i in l:
    print(i.get_text(strip = True))  #글만 가져오고 나머지 쳐내는 strip = True 사용


    
##선생님
from bs4 import BeautifulSoup
import urllib.request as req

url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")
result = soup.find_all('p', class_="con")
for i in result:
    print(i.get_text(strip=True))



url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
url = urllib.request.Request(url)
res = urllib.request.urlopen(url).read().decode("utf-8")
soup = BeautifulSoup(res,"html.parser")
result = soup.find_all('p', class_="con")
for i in result:
    print(i.get_text(strip=True))



[문제181] 게시글 뿐만 아니라 게시날짜 정보도 같이 출력하시오 !

2017.04.12 19:48 레이디버그 3기나오면 좋은사람 손~~

url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser")

"""
l1 =soup.findAll('p',{'class' : 'con'})  #class값 추가해서 찾아내기
for i in l1:
    print(i.get_text(strip = True))

l2 =soup.findAll('span',{'class' : 'date'})  #class값 추가해서 찾아내기
for i in l2:
    print(i.get_text(strip = True))
""" 
l1 =soup.findAll('p',{'class' : 'con'})  
l2 =soup.findAll('span',{'class' : 'date'})  

cnt = 0
for i in l1:
    print(l2[cnt].text, i.get_text(strip = True))
    cnt += 1


##선생님
from bs4 import BeautifulSoup
import urllib.request as req
url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
res = req.urlopen(url)
soup= BeautifulSoup(res, "html.parser")
a = soup.find_all('p',class_="con")
b = soup.find_all('span',class_="date")
print(b[0].get_text())
print(b[0].text)

cnt= 0
for i in a:
    print(b[cnt].text,i.get_text(strip=True))
    cnt += 1

print(cnt)


[문제182] 게시판에 게시글 전부를 수집해주세요.

#게시판 전부 다
for i in range(1,17):
    url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(i)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    
    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser")
    
    l =soup.findAll('p',{'class' : 'con'})
    for i in l:
        print(i.get_text(strip = True))  #글만 가져오고 나머지 쳐내는 strip = True 사용
    

##쌤꺼
for i in range(1,16):
    url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=" +str(i)+ "&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"

    res = req.urlopen(url)
    soup= BeautifulSoup(res, "html.parser")
    a = soup.find_all('p',class_="con")
    b = soup.find_all('span',class_="date")
    cnt= 0
    content =[]
    for i in a:
        content.append(b[cnt].text + i.get_text(strip=True))
        cnt += 1
    
    for j in content:
        print(j)



[문제183] 게시판에 게시글 전부를 수집한 후 공백문자를 기준으로 분리한후 빈도수를 체크해 주세요.

a = []
for i in range(1,17):
    url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page="+str(i)+"&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"
    
    res = req.urlopen(url)
    soup = BeautifulSoup(res,"html.parser")
    
    l =soup.findAll('p',{'class' : 'con'})
    for i in l:
        text = i.get_text(strip = True)
        a.append(text.split(" "))
       


for i in a:
    print(i)
    
a
a.split(' ')

##쌤꺼
import urllib.request
from bs4 import BeautifulSoup

lst = []

for i in range(1,16):
    url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=" +str(i)+ "&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&"

    res = req.urlopen(url)
    soup= BeautifulSoup(res, "html.parser")
    result = soup.find_all('p',class_="con")
   
    for i in result:
        lst.append(i.get_text(strip=True))
    print(lst)




fre = {}
for i in lst:
    w = i.split()
    for j in w:
        if j in fre:
            fre[j] += 1
        else:
            fre[j] = 1
               

for k,v in fre.items():
    if v >=10 :
        print(k,v)
for k,v in fre.items():
     print(k,v)


[문제184] 동아일보 크롤링
 
import urllib.request
from bs4 import BeautifulSoup

lst = []

url = "http://news.donga.com/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"

res = req.urlopen(url)
soup= BeautifulSoup(res, "html.parser")

# link 따오기
a = []
for link in soup.findAll('a',attrs = {'href':re.compile('http://news.donga.com/3/')}):
    a.append(link.get('href'))    
a = set(a)   #중복되는것들 제거

tt =[]
for i in a:
    url = i
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    
    l =soup.findAll('div',{'class' : 'article_txt'})
    for i in l:
        text = i.get_text(strip = True)
        print(text[0:text.find('function')])
        tt.append(text[0:text.find('function')])
        print("========================================================================")
tt

##쌤꺼
import urllib.request
from bs4 import BeautifulSoup

params = []

for i in range(1,2):
    list_url = "http://news.donga.com/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1"

    url = urllib.request.Request(list_url)
    res = urllib.request.urlopen(url, timeout=100).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    for j in range(0,15):
        soup2 = soup.find_all('p', class_="tit")[j]
        #print(soup2)
        soup3 = soup2.find('a')['href']
        #print(soup3)
        params.append(soup3)

print(params)


cn = 0
txt= []
for i in params:
    print(i)
    url = urllib.request.Request(i)
    res = urllib.request.urlopen(url).read().decode("utf-8")
    soup= BeautifulSoup(res, "html.parser")
    result = soup.find_all('div',class_='article_txt')
    
    
    for i in result:
        #print(i.text)
       txt.append(i.text)


for i in range(0,15):
    print(txt[i][0:txt[i].find('function getNewsLikeCount')])


