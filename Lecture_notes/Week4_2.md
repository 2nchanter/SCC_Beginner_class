## 11. [나홀로메모장] - API 설계하기
### 18) 프로젝트 설계 - 만들 API 설계
- API 설계를 우선적으로 하는 이유는,
<br> 우리 서비스에 어떤 기능이 필요한지, 어떤 순서로 구현 할 예정인지 설계해야 함.
<br> 1. url, comment를 서버에 보내서 db에 저장하는 것
<br> - 이미지, 제목, (링크), 요약, 코멘트를 저장
<br> 2. 카드들을 보여주는 것

- **포스팅API  - 카드 생성 (Create)
<br> **A. 요청 정보**
<br> - 요청 URL= `/memo`, 요청 방식 = `POST`
<br> - 요청 데이터 : URL(url_give), 코멘트(comment_give)
<br> **B. 서버가 제공할 기능** 
<br> - URL의 meta태그 정보를 바탕으로 제목, 설명, 이미지URL 스크래핑
<br> - (제목, 설명, URL, 이미지URL, 코멘트) 정보를 모두 DB에 저장
<br> **C. 응답 데이터**
<br> - API가 정상적으로 작동하는지 클라이언트에게 알려주기 위해서 성공 메시지 보내기
<br> - (JSON 형식) 'result'= 'success'

- **리스팅API - 저장된 카드 보여주기 (Read)
<br> **A. 요청 정보**
<br> - 요청 URL= `/memo` , 요청 방식 = `GET`
<br> - 요청 데이터 : 없음
<br> **B. 서버가 제공할 기능** 
<br> - DB에 저장돼있는 모든 (제목, 설명, URL, 이미지URL, 코멘트) 정보를 가져오기
<br> **C. 응답 데이터**
<br> - 아티클(기사)들의 정보(제목, 설명, URL, 이미지URL, 코멘트) → 카드 만들어서 붙이기
<br> - (JSON 형식) 'articles': 아티클 정보

## 12. [나홀로메모장] - 조각 기능 구현해보기
### 19) 프로젝트 준비 - URL 에서 페이지 정보 가져오기(**meta태그 스크래핑**)
- 이렇게, API에서 수행해야하는 작업 중 익숙하지 않은 것들은, 따로 python 파일을 만들어 실행해보고, 잘 되면 코드를 붙여넣는 방식으로 하는 게 편합니다.

- Code : [mini_projects/alonememo/](https://github.com/2nchanter/SCC_Beginner_class/tree/main/mini_projects/alonememo)
