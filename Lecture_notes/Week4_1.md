## 01. 4주차 오늘 배울 것
### 1) Flask, 미니프로젝트1, 2
- 동일 PC에서 서버도 만들고, 브라우저로 요청도 하는 "로컬 개발환경"

## 03. Flask시작하기 - 서버만들기
### 3) Flask 기초: 기본 실행
- Flask 프레임워크는 Jinja2 템플릿엔진을 기본적으로 사용.
<br> jinja2를 사용하면 render_template() 함수를 이용하여 HTML을 렌더링 할 수 있다.

- **프레임워크(Flask)** → 남이 짜둔 어떤 규칙이나, 틀 안에서 내가 코딩을 자유롭게 한다.
<br> **라이브러리** → 내가 내맘대로짜는데, 남이 만들어 놓은 것을 중간에 자유롭게 갖다 쓴다.
<br> 그래서 통상적으로 하나의 프레임워크 안에서 짜되, 안에 라이브러리가 잔뜩 들어간다.
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return '나의 첫 서버.'

# localhost:5000 뒤에 /mypage를 치면 새로운 페이지 등장
@app.route('/mypage')
def mypage():
   return '<button>나는 버튼이다</button>'
# 위와 같이 html을 작성하면 연습한대로 나오는데,
# 여기다 작성하면 너무 기니까 우리는 flask라는 프레임워크를 사용한다.

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
```

## 04. Flask시작하기 - HTML파일 주기
### 5) Flask 기초: 기본 폴더구조
- 프로젝트 폴더 안에,
<br> **ㄴstatic 폴더** (이미지, css파일)
<br> **ㄴtemplates 폴더** (html파일)
<br> **ㄴapp.py 파일

`+) flask 프레임워크에 venv안에  pymongo, bs4, requests 패키지 확인**`

- **과정!**
<br> 클라이언트가 브라우저에 주소 엔터 침 - app.py @app.route로 들어오면서 home함수를 실행함 - return에 render_template(여기)있는걸 돌려 줌. - 화면에 딱!

- 기존에는 html 파일을 열었지만, 지금은 서버에 요청한 화면을 연 것.
<br> 이제 확인시 크롬 아이콘이 아니라 서버에 직접 [요청](http://localhost:5000/)해서 열어보자!

## 05. Flask시작하기 - 본격 API 만들기
### 7) GET, POST
- GET  →  통상적으로! 데이터 조회(Read)를 요청할 때
<br> 예) 영화 목록 조회
<br> → **데이터 전달** : URL 뒤에 물음표를 붙여 key=value로 전달
<br> → 예: google.com?q=북극곰
- POST → 통상적으로! 데이터 생성(Create), 변경(Update), 삭제(Delete) 요청 할 때
<br> 예) 회원가입, 회원탈퇴, 비밀번호 수정
<br> → **데이터 전달 :** 바로 보이지 않는 HTML body에 key:value 형태로 전달
- 과정
**Ajax** : call (url) → **API** : url ? 뒤의 데이터 받음 / return jsonify → **Ajax** : 받아서 return response
#### Code (url, data 작성 방식 다름)
```python
# GET
@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

#POST
@app.route('/test', methods=['POST'])
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})
```
```jsx
// GET
function showReview() {
    $.ajax({
	      type: "GET",
	      url: "/test?title_give=봄날은간다",
	      data: {},
	      success: function(response){
	         console.log(response)
	      }
 	  })
}

// POST
function makeReview() {
		$.ajax({
		    type: "POST",
		    url: "/test",
		    data: { title_give:'봄날은간다' },
		    success: function(response){
		       console.log(response)
		    }
	  })
}
```

## 08. [모두의책리뷰] - POST 연습(리뷰 저장)
### 13) API 만들고 사용하기
`제목, 저자, 리뷰 정보 저장하기(Create → **POST**)`
1. 클라이언트와 서버 확인하기
2. 서버부터 만들기
3. 클라이언트 만들기
4. 완성 확인하기

- **API 정보 기획하기.**
<br> [리뷰 저장하기(Create)]
<br> **A. 요청 정보**
<br> - 요청 URL= `/review` , 요청 방식 = `POST` 
<br> - 요청 데이터 : 제목(title), 저자(author), 리뷰(review)
<br> **B. 서버가 제공할 기능**
<br> - 클라이언트에게 보낸 요청 데이터를 데이터베이스에 생성(Create)하고, 저장이 성공했다고 응답 데이터를 보냄
<br> **C. 응답 데이터  :** (JSON 형식) 'result'= 'success',  'msg'= '리뷰가 성공적으로 작성되었습니다.'
<br> - JSON 형식?
<br> JavaScript Object Notation (JSON)은 Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷입니다. **웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용**합니다(서버에서 클라이언트로 데이터를 전송하여 표현하려거나 반대의 경우).
- Code : [mini_projects/bookreview/](https://github.com/2nchanter/SCC_Beginner_class/tree/main/mini_projects/bookreview)

## 09. [모두의책리뷰] - GET 연습(리뷰 보여주기)
### 14) API 만들고 사용하기
`저장된 리뷰를 화면에 보여주기(Read → GET)`

- **API 정보 기획하기.**
<br> [리뷰 보여주기(Read)]
<br> **A. 요청 정보**
<br> - 요청 URL= `/review` , 요청 방식 = `GET` 
<br> - 요청 데이터 : 없음
<br> **B. 서버가 제공할 기능** :  데이터베이스에 리뷰 정보를 조회(Read)하고, 성공 메시지와 리뷰 정보를 응답 데이터를 보냄
<br> **C. 응답 데이터  :** (JSON 형식) 'result'= 'success',  'reviews'= 리뷰리스트
- Code : [mini_projects/bookreview/](https://github.com/2nchanter/SCC_Beginner_class/tree/main/mini_projects/bookreview)
