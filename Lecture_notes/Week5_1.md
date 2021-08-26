## 01. 설치
### *) Filezilla, 가비아 도메인 구입

## 04. **[moviestar] - DB 만들기(데이터 쌓기)**
### 3) 프로젝트 준비 - 프로젝트에서 사용할 데이터 넣기(웹 스크래핑)
- 어떤 데이터를 먼저 모아두고, 그것을 보여주는 작업은 많이 이용된다.

## 06. [moviestar] - GET연습(보여주기)
### 5) 문제 분석 - 화면과 동작 살펴보기
- 우리가 만들 기능은 `영화인 정보를 카드로 보여주기(Read)` 입니다.
- **화면에 어떤 데이터가 어떤 부분에 보여지는지** 영화인 카드 화면 코드를 보며 분석해보겠습니다.
<br> - 영화인 이름
<br> - 영화인 이미지 : 이미지 src 속성
<br> - 좋아요 개수
<br> - 최근 작품 내용이 들어가는 부분
<br> -> index.html을 크롬에서 실행시켜 크롬 개발자도구 - 검사하기(Inspector)로 
<br> 어떤 요소에 어떤 데이터가 보일지 분석해보세요.
<img src="https://user-images.githubusercontent.com/89369520/130970486-19c357af-cd0c-442d-a8d6-918f4b24d27e.png" height="250">

### 6) API 만들고 사용하기 - 영화인 조회 API (Read → GET)
- 만들 API
<br> 1. 조회(Read) 기능: 영화인 정보 전체를 조회
<br> 2. 좋아요(Update) 기능: 클라이언트에서 받은 이름(name_give)으로 찾아서 좋아요(like)를 증가
<br> 3. 삭제(Delete) 기능: 클라이언트에서 받은 이름(name_give)으로 영화인을 찾고, 해당 영화인을 삭제

#### mongodb 내림차순
```python
Sort Descending
Use the value -1 as the second parameter to sort descending.

find().sort("name", 1) #ascending
find().sort("name", -1) #descending
```

## 07. [moviestar] - POST연습(좋아요+1)
### 7) API 만들고 사용하기 -  좋아요 API (Update → **POST**)

## 08. [moviestar] - POST연습(삭제하기)
### 8) API 만들고 사용하기 -  카드 삭제 API (Delete → **POST**)

- Code : [mini_projects/moviestar/](https://github.com/2nchanter/SCC_Beginner_class/tree/main/mini_projects/moviestar)
