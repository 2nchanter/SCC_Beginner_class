## 01. 서버/클라이언트/웹의 동작 개념
### 1) 서버/클라이언트/웹의 동작 개념
`네이버 웹페이지에 오른쪽 키 - 검사 - 글씨 바꿔보기`
- 내가 보는 맵페이지 글씨를 바꿀 수 있었다.
- 다른 페이지를 눌렀을때 인터넷이 끊기더라. -> 내가 보고있는 화면과 인터넷은 관계가 없다.
- 새로고침 누르면 원상복귀 된다. -> 서버로부터 다시 받아온다.
<br> = 서버에게 요청 (url치고 enter) -> 결과물을 받아서 그려준다.

### 2) 웹의 동작 개념 - HTML을 받는 경우
<img src="https://user-images.githubusercontent.com/89369520/130933118-f96d5855-b11a-4a90-8f3b-32454eb6f134.png" height="300">

### 3) 웹의 동작 개념 - 데이터만 받는 경우
`Pycharm / Jetbrains / AWS 설치.`
- 기본적으로 서버는 클라이언트한테 그릴 것을 줌.
<br> '그릴 것'은 사실 데이터인데, 전체 갱신 말고 딱 '데이터'만 받아오고 싶은 경우,
<br> JSON 형식으로 받아온다. ex) 티켓팅

## 03. HTML
### 7) HTML과 CSS의 개념, 기초
- HTML : 구역과 텍스트를 나타내는 코드
<br> head : 페이지의 속성 정보 (meta, script, link, title 등)
<br> body : 페이지의 내용
```
   div : division 구역 분할 
   p : paragraph 문장
   h1 : 제목 / page마다 하나씩 있는것이 좋음(가져갈 수 있도록)
   span : 특정구역 묶을때.
   a : hyperlink
   hr : 가로선
```
- CSS : 구역과 텍스트를 꾸며주는 코드
<br> 인라인 스타일(Inline style)
<br> 내부 스타일 시트(Internal style sheet)
<br> 외부 스타일 시트(External style sheet)

## 04. Quiz_간단한 로그인 페이지 만들어보기
### 9) 로그인 페이지
- 쉽게 쉽게 복사해서 만들어보자.
<br> 전체선택 : `cmd + a`
<br> 자동정렬 : `cmd + opt + l`
<br> 줄바꾸기 : `<p>`
<br> 버튼 : `<button>`
<br> 빈칸 : `<input type="text" />`

- Code : [01_login.html](https://github.com/2nchanter/SCC_Beginner_class/blob/main/frontend_prac/01_login.html)

## 05. CSS 기초
### 10) HTML 부모-자식 구조 살펴보기, CSS 기초
- html 태그는, "누가 누구 안에 있느냐"를 이해하는 것이 가장 중요
- 작성법
	- `<head> ~ </head>` 안에 `<style> ~ </style>` 로 공간을 만듬.
- 자주 쓰이는 것들!
```
   배경관련 : background-color, background-image, background-size
   사이즈 : width, height
   폰트 : font-size, font-weight, font-famliy color
   간격 : margin, padding
```

## 06. 자주 쓰이는 CSS 연습하기
### 12) 주요 CSS
- 연습할 것들
`h1, h5, background-image, background-size, background-position
color, width, height, border-radius, margin, padding`
```
   - padding : 안으로
   - margin - 밖으로 (margin-top: 위에만,,!)
     ex) margin: 20px 0px 0px 30px (TRBL 시계방향 순서)
 
   - html에는 글속성, 박스속성이 있음.
     글속성 -> 박스속성으로 강제로 바꿔줌 -> 옮김.
     ex) display: block;
      
    - class에는 중첩 개념이 있음, 명찰을 두개 주면 된다.
     ex) "mybtn red-font"
```
<img src="https://user-images.githubusercontent.com/89369520/130935054-c83c9a48-d3b6-47bd-958b-f5e2037294f2.png" height="300">

## 07. 폰트, 주석, 파일분리
### 13) 구글 웹폰트
- 폰트 : [https://fonts.google.com/?subset=korean](https://fonts.google.com/?subset=korean)
- link 태그 → `<head> ~ </head>` 사이에 (title 아래)
- CSS → `<style> ~ </style>` 사이에 (style 아래 * {...} : 모든 태그에 다 먹힘)
### 14) 주석 달기
- 임시로 작동하지 못하게 막음
  : `opt + cmd + /`
```
   <!-- 설명을 적어주면 좋다 -->
```
### 15) CSS 파일 분리
- 한눈에 보기 편하게,
```html
   <!-- style.css 파일을 같은 폴더에 만들고, head 태그에서 불러오기 -->
   <link rel="stylesheet" type="text/css" href = "(css파일이름).css">
```

## 08 부트스트랩, 예쁜 CSS 모음집
### 16) bootstrap?

- 예쁜 CSS를 미리 모아둔 것.
<br> 사용시 시작 템플릿을 가지고 시작해야됨 (JS, CSS, 다 들어있다)
<br> 복사본 + 내가 커스텀 하면 된다.
<br> : 부트스트랩 컴포넌트 4.0 :   [https://getbootstrap.com/docs/4.0/components/alerts/](https://getbootstrap.com/docs/4.0/components/alerts/)

- body에 복사해서 쓰되, 너무 많아서 어떤 것을 사용해야 할지 모를 때는 오른쪽 키, 검사.
<br> 아예 모를 때는 구글에 검색.(ex. css 폰트 변경)

## 10. Quiz_나홀로메모장+포스팅박스
### 19) 나홀로 메모장
- Code : [index.html](https://github.com/2nchanter/SCC_Beginner_class/blob/main/frontend_prac/index.html)
