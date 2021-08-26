## 10. DB설치 확인
### - 11) mongoDB, robo 3T?
- mongoDB : 데이터베이스. 내눈에 보이지는 않게 켜짐.
- robo 3T : mongoDB를 시각화해서 보여줌.

## 11. DB개괄
### *) 일단 왜 쓰는걸까?
```
데이터를 잘 찾아서 갖다 쓰기 위함. 그래서 잘 쌓아둬야함.
상황에 따라 맞는 데이터베이스 프로그램이 있음.

서버 = 컴퓨터의 역할
DB도 프로그램 켜서 쓰는 것으로 생각하면 됨.
```

### 13) 들어가기 전에 : DB의 두 가지 종류
<img src="https://user-images.githubusercontent.com/89369520/130965560-e865eefb-e6e4-4aee-8926-d5e34fc14c0b.png" height="300">

- RDBMS(Relational DataBase Management System, 관계형 데이터베이스 관리 시스템)
<br> : 칸을 미리 만들어두고 채워나가는 엑셀과 비슷.
<br> 열, 행을 미리 정해둬야 하기 때문에 **정형화된 데이터 뽑을 때, 분석할 때 편리.**
<br> → (SQL) MS-SQL, My-SQL, Oracle
- No-SQL (not only Structured Query Language)
<br> : 한줄한줄이 딕셔너리 형태로 들어감
<br> 공란이 필요 없으므로, 유연한 데이터베이스 방식,  일관성 부족
<br> 아직 형태가 없으므로, 스타트 업이나 초기 세팅에 많이 쓰임.
<br> → MongoDB

## 12. pymongo로 DB조작하기
### 15) pymongo 사용법. 코드요약
```python
# pymongo를 사용하겠습니다.
# 내 pc에서 돌아가고 있는 mongoDB에 접속할겁니다.
#dbsparta라고 되어있는 이름으로 접속할겁니다. (없으면 자동으로 만들어짐)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
```

## 13. 웹스크래핑 결과 저장하기
### 16) insert 연습하기 - 웹스크래핑 결과를 DB에 저장하기
- pymongo를 import 해주고, 도큐먼트 만들어 하나씩 insert 하기
- Code : [python_prac/hello.py](https://github.com/2nchanter/SCC_Beginner_class/blob/main/python_prac/hello.py)

## 14. Quiz_웹스크래핑 결과 이용하기
### 17) find, update 연습하기
- Code : [python_prac/dbquiz.py](https://github.com/2nchanter/SCC_Beginner_class/blob/main/python_prac/dbquiz.py)

## 15. 3주차 과제
### *) 지니뮤직 1~50위 곡 스크래핑
- .strip() - 공백 제거
<br> .변수명[0:2] - 두번째 자리까지만 출력
- Code : [python_prac/genie.py](https://github.com/2nchanter/SCC_Beginner_class/blob/main/python_prac/genie.py)
