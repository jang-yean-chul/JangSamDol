from bs4 import BeautifulSoup

html = """
<ul id = '조선왕'>
<li id = '태조'> '이성계' </li>
<li id = '정종'> '이방과' </li>
<li id = '태종'> '이방원' </li>
<li id = '세종'> '이도' </li>
<li id = '문종'> '이향' </li>
</ul>
"""

soup = BeautifulSoup(html,"html.parser")

soup.select_one('li[id="세종"]').text  #어떤태그의 내용을 하나 뽑아내겠다., 가운데 띄워쓰기하면 안먹힘.
soup.select_one('li[id="세종"]').string
soup.select_one('#세종').text
soup.select_one('li#세종').text
soup.select_one('ul > li#세종').text
soup.select_one('#조선왕 #세종').text
soup.select_one('ul#조선왕 > li#세종').text
soup.select_one('li:nth-of-type(1)').text
soup.select_one('li:nth-of-type(2)').text

lst = soup.select('li')
for i in lst:
    print(i.text)

soup.select('li')[0].string
soup.find_all('li')[0].string


file = open("c:/python/sale.html",encoding = "utf=8")

soup = BeautifulSoup(file, "html.parser")

soup.select_one("li:nth-of-type(6)").string
soup.select_one("#vegetable > li:nth-of-type(2)").string
soup.select_one("#vegetable > li.red").string

soup.select_one("#vegetable > li.green").string
soup.select("#vegetable > li.green")[0].string

soup.select_one("li:nth-of-type(4)").string
soup.select("#fruits > li.yellow")[1].string
soup.select("li.yellow")[1].string
soup.select("li.green")[2].string

condition = {"data-lo":"us","class":"red"}

soup.find("li",condition).string

soup.find(id = "vegetable").find("li",condition).string

https://ko.wikisource.org


import urllib.request as req
from bs4 import BeautifulSoup
import os
from os.path import exists


url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%ED%95%9C%EC%9A%A9%EC%9A%B4"
res = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")

soup.select_one("#mw-content-text > div > ul:nth-child(9) > li:nth-child(1) > a").string   #select에서 사용할수없는 method다.

                
l = soup.select("#mw-content-text > div > ul > li > a")                

for i in l:
    print(i.string)
                                
for i in l:
    print(i.get_text(strip = True))
                



from urllib.request import urlopen

url = "http://img.hani.co.kr/imgdb/resize/2018/0328/152214693895_20180328.JPG"

imgname = url.split('/')[-1]

with urlopen(url) as f:
    with open("c:/python/" + imgname, 'wb') as w:     # write를 하되 binary형태로 하라는 wb를 사용
        img = f.read()
        w.write(img)

=======================================================================================

selenium 
    웹 브라우저를 컨트롤하여 웹 UI(User Interface)를 지정하는 도구
    웹 자동화

selenium 설치
pip install selenium  #cmd에서 실행

selenium 드라이버 설치

http://phantomjs.org/  접속
webdriver.Firefox
webdriver.Chrom
webdriver.le
webdriver.Opera
webdriver.PhantomJS(CLI(command line interface) 형식의 브라우저)

# 사용할 webdriver를 import한다.
from selenium import webdriver

url = "http://www.hani.co.kr/"

# phantomjs 드라이버 추출
driver = webdriver.PhantomJS("C:/Python/phantomjs-2.1.1-windows/bin/phantomjs.exe")

# 드라이버를 초기화 될때까지 3초간 대기
driver.implicitly_wait(3)

# 웹페이지 읽어 들이기
driver.get(url)

# 스샷 저장
driver.save_screenshot("c:/python/hani.png")

# 드라이버 종료 브라우저를 닫는다.
driver.quit()

######################################################################
chromedriver.exe
https://sites.google.com/a/chromium.org/chromedriver/downloads


from selenium import webdriver

# chromedriver 드라이버 추출
driver = webdriver.Chrome("C:/Python/chromedriver.exe")

# 드라이버를 초기화 될때까지 3초간 대기
driver.implicitly_wait(3)

# 웹페이지 읽어 들이기
driver.get(url)

# 스샷 저장
driver.save_screenshot("c:/python/hani.png")

# 드라이버 종료 브라우저를 닫는다.
driver.quit()



####네이버 접속

# 아이디하고 비밀번호 입력
user = ""
mypass = ""

#  불러오기
#driver = webdriver.PhantomJS("C:/Python/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver = webdriver.Chrome("C:/Python/chromedriver.exe")

#로그인할곳 찾기
driver.implicitly_wait(3)
url = "https://nid.naver.com/nidlogin.login"
driver.get(url)

#input 요소를 찾는 메소드, id 요소값을 찾는 메소드 (아이디 입력)
inputid = driver.find_element_by_id("id")
inputid.clear()     # id값 비우기
inputid.send_keys(user)     # send key라는 메소드를 이용해 id를 입력한다

#패스워드 입력
inputpw = driver.find_element_by_id("pw")
inputpw.clear()
inputpw.send_keys(mypass)

#로그인 버튼 찾기
loginbtn = driver.find_element_by_css_selector("input.btn_global[type = submit]")
# 아이디하고 비밀번호 전송
loginbtn.submit()

#사이트 가져오기
driver.get("https://pay.naver.com/")
html = driver.page_source

soup = BeautifulSoup(html,"html.parser")
lst = soup.find_all('table',class_ = "")

for i in lst:
    print(i.text)

#종료!
driver.quit()




#driver = webdriver.PhantomJS("C:/Python/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver = webdriver.Chrome("C:/Python/chromedriver.exe")
driver.implicitly_wait(3)
driver.get("http://google.com")
#res = driver.execute_script("return 10 + 20")
#print(res)
driver.execute_script("window.alert('오늘 하루도 행복하자')")


selenium 으로 DOM요소를 선택하는 방법

DOM(Document Object Model) 은 html / xml 문서를 처리하는 API

find_element_by_id("id") : id속성으로 요소를 하나 추출
find_element_by_name("name") : name 속성으로 요소를 하나 추출
find_element_by_css_selector(query) : css선택자로 요소를 하나 추출
find_element_by_css_xpath(query) : xpath를 지정해서 요소 하나를 추출
find_element_by_tag_name(name) : tag name을 지정해서 요소하나를 추출
find_element_by_link_text(text) : 링크텍스트로 요소 하나를 추출
find_element_by_partial_link_text(text) : 링크의 자식요소에 포함되어있는 텍스트로 요소 하나를 추출
find_element_by_class_name(name) : 클래스 이름에 해당하는 요소 하나를 추출


# DOM내부에 있는 여러개의 요소들을 모두 추출하는 메소드
find_element_by_css_selector(query)
find_element_by_css_xpath(query)
find_element_by_tag_name(name)
find_element_by_class_name(name)
find_element_by_partial_link_text(text)

# DOM 요소에 적용 할 수 있는 메소드
clear() : 글자를 입력할 수 있는 요소의 글자를 지운다.
click() : 요소를 클릭
get_attribute(name) : 요소의 속성중에 name에 해당되는 속성의 값을 추출
screenshot(filename) : 화면을 캡쳐해서 이미지 파일로 저장
send_keys(value) : 키를 입력 보낸다. 텍스트 데이터로 보낸다.


value가 텍스트 데이터가 아닌경우(특수키,함수키,enter,tab,ctrl)
from selenium.webdriver.common.keys import Keys
ARROW_DOWN / ARROW_LEFT / ARROW_RIGHT / ARROW_UP / BACKSPACE / DELETE / HOME / END / INSERT
ALT / COMMAND / CONTROL / SHIFT / ENTER / ESCAPE / SPACE / TAB / F1~F12

submit() : 입력 양식을 전송
value_of_css_property(name) : name 해당하는 css속성 값을 추출



