## 07. 서버-클라이언트 통신 이해하기
### 8) 서버→클라이언트: "JSON"을 이해하기
- JS로 페이지 전환 없이 서버에서 값을 받아보자.
<br> JSON은 Key-Value로 이루어짐, dict & list 조합과 유사함.
- for문의 전형적인 형태, 가져다 쓸 수 있다.
<img src="https://user-images.githubusercontent.com/89369520/130962094-dc5029d6-3835-4366-be52-37f80265d1c1.png" height="200">

### 9) 클라이언트→서버: GET 요청 이해하기
- 서버에서 클라이언트에게 열어놓은 창구, API.
<br> GET : 데이터 조회(Read) - 영화목록조회
<br> POST : 생성(Create), 변경(Update), 삭제(Delete) - 회원가입, 탈퇴, 수정
```jsx
   google.com/search?q=아이폰&sourceid=chrome&ie=UTF-8

   은행지점명 ~ 창구 ~ "?" ~ 가지고 가려는 데이터
   <서버 주소> "?" q=검색어 & sourceid=브라우저 정보 & ie=인코딩 정보

   프론트엔드 와 백엔드 개발자의 약속.
```

## 08. Ajax 시작
### *) Ajax 기본 골격 code
```jsx
// jQuery import 되어있어야 사용 가능 !

$.ajax({
    type: "GET",
    url: "여기에URL을입력",
    data: {},
    success: function (response) {
    console.log(response)
    }
})
```

### 12) 서울시 OpenAPI(실시간 미세먼지 상태)를 이용하기
`참고! Ajax는 jQuery를 임포트한 페이지에서만 동작 가능`
- Ajax 코드 해설 (그냥 이렇게 생긴 애구나, 받아들이기, 스트레스 받지 말기!)
<br> *어 뭐야 쓰다보니 외워지네 ㄷ*
```jsx
$.ajax({
  type: "GET", // GET 방식으로 요청
  url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
  data: {}, // POST 방식 시 사용 (요청하면서 함께 줄 데이터)
  success: function(response){ // 서버에서 준 결과를 response라는 변수에 담음
    console.log(response) // 여기서 for, if 등 요리해보자.
  }
})
```

## 09. Ajax 연습
### 13) Ajax 기본 사용 code
- Code : [frontend_prac/02_Ajaxquiz01.html](https://github.com/2nchanter/SCC_Beginner_class/blob/main/frontend_prac/02_Ajaxquiz01.html)

## 12. 2주차 과제
### *) 1주차 + 로딩시 달러 환율 표기
- Code : [frontend_prac/02_HW.html](https://github.com/2nchanter/SCC_Beginner_class/blob/main/frontend_prac/02_HW.html)
