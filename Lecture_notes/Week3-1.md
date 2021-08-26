## 02. 3주차
### *) Python / mongoDB / Robo3T (+ 설치 / 크롤링)
- 4, 5주차에 서버를 만드는데, python을 이용해서 pc에 서버 역할을 요청.
- 데이터를 담을 곳이 필요, mongoDB.

## 03. OpenAPI 복습
### *) 생각하는 과정
loading이 되고
<br> listing 함수가 불러지고
<br> 넣어준 url값에 Ajax콜이 되고
<br> 그 결과를 response에 받아와서
<br> for문으로 돌면서 원하는 데이터만 뽑아서 선언해주고
<br> 선언해준 것들을 모아서 temp_html에 갱신해줄 골격을 만들고
<br> .append로 body 내 id에 넣어준다.
<br> * 로딩시 .empty(); 로 id 내부 날려주는 것도 확인.

## 04. 파이썬 시작하기
### 3) Python?
- 010000110 → 가능한 사람이 쉽게 사용 가능한 언어로 변경해주는 '번역팩' / 범용성, 진입장벽이 낮음 = Python
- venv 파일은 건드리지 말 것.
- 위에 초록 play 버튼말고, 오른쪽키 - Run 을 누르는 습관.
- 모든 문법을 다 알 수 가 없다. 필요할 때 구글링 하는 습관을 들이자!

## 05. 파이썬 기초공부
### 6) 파이썬 기초 문법 (+ pip requests pkg 설치, AP의 팁!)
`() function, {} array, [] data / def:, if:, else if:, for:`

#### 변수, 자료형, 함수, 조건문, 반복문
```python
#변수
a = 3
b = 2 # print(a + b) -> 5

#list
a_list = []
a_list.append(1)
a_list.append([2,3]) # print(a_list) -> [1,[2,3]]

#dict
a_dict = {}
a_dict = {'name':'bob','age':21}
a_dict['height'] = 178 # 

#함수, 조건문, 반복문
💡 # for : list를 하나씩 빼서 모두 사용하면 종료. 무조건 list와 같이 쓴다.
people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

#이름을 받아 나이를 출력해보자.
#person에 people에서 list 내 dict를 한줄찍 받아서
#if 이름이 같다면
#나이를 return해달라
#다 돌았는데 이름이 없다? 다시써달라.
def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'

print(get_age('bob'))
print(get_age('kay'))
```
- venv = 가상환경, 프로젝트 별로 패키지들을 담는 공구함

## 07. 패키지 사용해보기
### 8) requests?  (라이브러리 사용해보기 + List/Dictionary/함수/If/For문 연습)
- API에서 list를 받아올 때, JS는 .ajax, Python은 requests를 사용한다
- 파싱?
<br> 어떤 페이지(문서, html 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출해 가공하는 것을 말한다.

`requests는 파이썬으로 HTTP 호출하는 프로그램을 작성할 때 가장 많이 사용되는 라이브러리.
(vs selenium?)`
- requests의 원리
<br> 첫 응답만 받으며 추가 요청이 없음
<br> 단순한 요청에 최적화
<br> HTML응답을 받더라도, 이에 명시된 이미지/CSS/JavaScript 추가 다운을 수행하지 않지만 직접 다운로드 요청은 가능하다
- selenium의 원리
<br> 웹브라우저 자동화 툴
<br> javascript/css 지원, 기존 GUI 브라우저 자동화 라이브러리
<br> 사람이 웹서핑 하는 것과 동일한 환경이지만 그만큼 리소스를 많이 먹음
<br> 웹브라우저에서 HTML에 명시된 CSS/JavaScript를 모두 자동다운로드하여 적용
<br> selenium이 직접 하지 않고 크롬등의 툴을 가지고 사용하기 때문에 리소스를 많이 잡아먹음
#### python requests 패키지 구글링
```python
import requests # requests 라이브러리 설치 필요

#rjson에 openapi 데이터 전체 받은 다음,
r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

#gus에 row 값 아래로만 다시 받아서,
gus = rjson['RealtimeCityAir']['row']

#gu로 gus list 안 dict를 하나씩 받아오면서 if문 진행.
for gu in gus:
    gu_name = gu['MSRSTE_NM']
    gu_mise = gu['IDEX_MVL']
    if gu_mise > 50 :
        print(gu_name, gu_mise)
```

## 08. 웹스크래핑(크롤링) 기초
### *) 크롤링, 파싱, 스크래핑 사전적 정의
- 웹 크롤러
<br> 크롤링은 웹 인덱싱을 위해 WWW를 체계적으로 탐색해나가는 것을 의미합니다. 크롤러가 하는 행위(WWW를 탐색해나가는 행위 등) = ‘크롤링’
- 파싱 (Parsing)
<br> 웹 파싱은 웹 상의 자연어, 컴퓨터 언어 등의 일련의 문자열들을 분석하는 프로세스
- 웹 스크래핑 (Web scraping)
<br> 웹 스크래핑은 다양한 웹사이트로부터 데이터를 추출하는 기술을 의미
`결론 : ‘크롤러’는 **데이터 추출**의 의미보다 **웹 사이트를 탐색하고, 인덱싱 하는 것**에 더 중점적인 의미를 갖고 있는 것 처럼 보임.`

### 9) 웹스크래핑 해보기
- 두가지가 중요.
<br> 브라우저를 열지 않고 요청하는 것(requests).
<br> 내가 원하는 요소를 잘 솎아내는 것(bs4). select1, select
<br> : 크롬 개발자도구 → 검사 → Copy → Copy selector로 선택자 복사

#### 크롤링 기본세팅
```python
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('url',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
```
#### select / select_one의 사용법
```python
# 태그 안의 텍스트를 찍고 싶을 땐 → 태그.text
# 태그 안의 속성을 찍고 싶을 땐 → 태그['속성']

<a href="/movie/bi/mi/basic.nhn?code=171539" title="그린 북">그린 북</a>
title.text # 그린 북
title['href'] # /movie/bi/mi/basic.nhn?code=171539
```
```python
# 선택자를 사용하는 방법 (copy selector)
soup.select('태그명')
soup.select('.클래스명')
soup.select('#아이디명')

soup.select('상위태그명 > 하위태그명 > 하위태그명')
soup.select('상위태그명.클래스명 > 하위태그명.클래스명')

# 태그와 속성값으로 찾는 방법
soup.select('태그명[속성="값"]')

# 한 개만 가져오고 싶은 경우
soup.select_one('위와 동일')
```

## 09. 웹스크래핑(크롤링) 연습
### 10) 웹스크래핑 더 해보기 (순위, 제목, 별점)
```python
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        rank = tr.select_one('td:nth-child(1) > img')['alt']
        title = a_tag.text
        point = tr.select_one('td.point').text
        print(rank, title, point)
```
#### Q. 네이버 해축 팀순위가 크롤링이 안된다?
```python
<정리>
1.
크롤링 하려고 하는 사이트가 정적인지, 동적인지 보자.

1-a.
#wfootballTeamRecordBody 로 먼저 출력해보면, 
<div class="record_tbl" id="wfootballTeamRecordBody">
</div>
로 나오는데, 이는 동적으로 내용을 넣어주는 것.

1-b.
페이지의 다른 부분을 먼저 출력해보자.
trs = soup.select_one('#content > div.record_tab > ul > li.selected > a > span > span.title')
print(trs.text)
‘프리미어리그’라고 출력이 됨.

1-c. selenium(?)을 이용해보자. (검색 필요)

2. 동적으로 받아온다면, 사용되고 있는 API를 알아보자.
    거기서 직접 받아오자 !
```
#### Q. 'NoneType' Err?
def(함수)에서 result를 주지 않고, print로 끝내면 종종 생긴다.
<br> (찾던건 이게 아니었는데?)
