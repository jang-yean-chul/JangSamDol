konlpy

JPype
JPype1-0.6.2-cp36-cp36m-win_amd64를 다운받는다.

pip install konlpy

pip install jpype1


JAVA_HOME설정
내컴퓨터 > 속성 > 고급시스템 설정 > 환경변수 > 변수확인

오라클 들어가서 자바깔고

JAVA_HOME설정
내컴퓨터 > 속성 > 고급시스템 설정 > 환경변수 > 변수확인


from konlpy.tag import Twitter
t = Twitter()
text = t.pos("아버지가방에들어가신다", norm = True , stem = True)
text
norm : "그래욕ㅋㅋㅋ" -> 그래요
stem : "그렇다" 원형을 찾아 준다.


from konlpy.tag import Kkma
k = Kkma()
txt = "통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이다. 통찰력을 얻는 좋은 방법은 독서이다."
#문장분석
k.sentences(txt)
#명사분석
k.nouns(txt)
#형태소 분석
k.pos(txt)


from konlpy.tag import Hannanum
h = Hannanum()
h.nouns(txt)


from konlpy.tag import Twitter
t = Twitter()
t.nouns(txt)
t.pos(txt)


import nltk

from konlpy.corpus import kobill

file_ko = kobill.fileids()

#디렉토리를 찾아야한다
#윈도우 탐색 > kobill 검색
#C:\Users\stu\Anaconda3\Lib\site-packages\konlpy\data\corpus\kobill
#예제파일 위치 찾아서 문재인태통령 취임사 > 열어서 다른이름으로 저장 > UTF-8로 kobill에 저장

doc_ko = kobill.open("문재인대통령취임사.txt").read()
doc_ko

from konlpy.tag import Twitter
t = Twitter()
tokens_ko = t.nouns(doc_ko)
tokens_ko

ko = nltk.Text(tokens_ko)
#단어의 총 갯수
len(ko.tokens)
#중복되는 것 제거
len(set(ko.tokens))
#단어의 건수
ko.vocab()

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
font_name = font_manager.FontProperties(fname = "c:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family = font_name)

plt.figure(figsize = (12,6))
ko.plot(50)
plt.show()

#불용어 처리
stopword = [',' , '.' , '(',')' , '의' , '에' , '해' , '제']

ko = [word for word in ko if word not in stopword]
ko = nltk.Text(ko)
len(set(ko.tokens))
ko.vocab()

plt.figure(figsize = (12,6))
ko.plot(50)
plt.show()

#국민이라는 글자가 몇번 언급되었는지
ko.count("국민")

#주변단어 검색
ko.concordance("약속")

#문서내 연이어 사용되는 단어들
nltk.download() #all다운로드
nltk.download('stopwords')  #불용어 다운 받아야한다.
ko.collocations()

from nltk import collocations
from konlpy.utils import pprint

ko.collocations()

measures = collocations.BigramAssocMeasures()
finder = collocations.BigramCollocationFinder.from_words(ko)
pprint(finder.nbest(measures.pmi, 10))

##여기들어가서 배워서 하자 http://konlpy-ko.readthedocs.io/ko/v0.4.3/examples/collocations/










