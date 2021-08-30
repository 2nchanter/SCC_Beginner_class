## 09. 내 프로젝트를 서버에 올리기
### 10) "웹서비스 런칭" 에 필요한 개념 소개
- 언제나 요청에 응답하려면, 
<br> 1) 컴퓨터가 **항상** 켜져있고 프로그램이 실행되어 있어야하고, 
<br> 2) 모두가 접근할 수 있는 공개 주소인 공개 IP 주소(Public IP Address)로 나의 웹 서비스에 **접근할 수 있도록** 해야함.
<br> → 이를 위해 EC2 사용권을 구입한다.
- IP address? port?
<br> - IP 주소
<br> : 컴퓨터가 통신할 수 있도록 컴퓨터마다 가지는 고유한 주소
<br> 정확히는 네트워크가 가능한 모든 기기가 통신할 수 있도록 가지고 있는 특수한 번호
<br> 서버는 하나의 주소를 가지고 있음
<br> - 포트(port)
<br> : 하나의 IP에 여러 포트가 있는데, 하나의 포트에 하나의 프로그램을 실행시킬 수 있음 
- DNS?
<img src="https://user-images.githubusercontent.com/89369520/130972432-34f9c41c-d0ee-45bb-a471-55e92345028e.png" height="200">

## 10. AWS EC2 서버
### 11) EC2?
- =인스턴스
<br> OS Linux Ubuntu(open source) 설치
<br> 키페어 : 원격접속 키
### 13) EC2 접속
- SSH(Secure Shell Protocol)
<br> - 다른 PC에 접속할 때 사용하는 프로그램, 22번 port 열려있어야 접속 가능.
<br> - terminal로 접속
<br> \* 터미널을 열기 (spotlight에 terminal 입력)
<br> \* 방금 받은 내 Keypair의 접근 권한을 바꿔주기
```bash
sudo chmod 400 받은키페어를끌어다놓기 
```
- SSH로 접속하기
```bash
ssh -i 받은키페어를끌어다놓기 ubuntu@AWS에적힌내아이피
```
- 예) 아래와 비슷한 생김새!
```bash
ssh -i /path/my-key-pair.pem ubuntu@13.125.250.20
```
### 14) 간단한 리눅스 명령어
```bash
ls: 내 위치의 모든 파일을 보여준다.
pwd: 내 위치(폴더의 경로)를 알려준다.
mkdir: 내 위치 아래에 폴더를 하나 만든다.
cd [갈 곳]: 나를 [갈 곳] 폴더로 이동시킨다.
cd .. : 나를 상위 폴더로 이동시킨다.
cp -r [복사할 것] [붙여넣기 할 것]: 복사 붙여넣기
rm -rf [지울 것]: 지우기
sudo [실행 할 명령어]: 명령어를 관리자 권한으로 실행한다.
sudo su: 관리가 권한으로 들어간다. (나올때는 exit으로 나옴)

##윗화살표 누르면 바로 전 명령어 ㄷㄷㄷㅈ. 
```

## 11. 서버 세팅, AWS 포트 열기, flask 서버 실행
### 17) 서버환경 통일하기
```bash
# UTC to KST : 서버 시간을 한국 시간으로 맞춰주는 명령어
sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

# python3 -> python : 명령어를 3빼고 사용할 수 있게 하는 명령어
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# pip3 -> pip : pip3 설치 및 3빼고 사용할 수 있게 하는 명령어
sudo apt-get update
sudo apt-get install -y python3-pip
pip3 --version
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# port forwarding : 80포트로 들어오는 요청을 5000포트로 넘겨주는 명령어
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 5000

# MongoDB - install : mongodb 설치
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org

sudo mkdir -p /data/db

# MongoDB - run : 실행. 아무 반응이 없으면, 잘 실행된 것
sudo service mongod start
sleep 7
netstat -tnlp

# MongoDB set user, set conf file
mongo admin --eval 'db.createUser({user: "test", pwd: "test", roles:["root"]});'
sudo sh -c 'echo "security:\n  authorization: enabled" >> /etc/mongod.conf'
sudo sed -i "s,\\(^[[:blank:]]*bindIp:\\) .*,\\1 0.0.0.0," /etc/mongod.conf

sudo service mongod stop
sudo service mongod start
sleep 5
netstat -tnlp
```
- AWS 포트 열기 - AWS EC2 Security Group에서 인바운드 요청 포트를 열기
	- EC2 관리 콘솔 → Security Group → Edit inbound rules → 포트 추가
    - 80포트: HTTP 접속을 위한 기본포트
    - 5000포트: flask 기본포트
    - 27017포트: 외부에서 mongoDB 접속을 하기위한 포트
- flask 설치, 서버 실행
```bash
pip install flask
python app.py
http://[내 EC2 IP]:5000/
```
- 포트포워딩?
	- 우리는 5000포트에서 웹 서비스가 실행되고 있으므로,
   http 요청시 들어오는 80요청을 5000으로 전달하게 해줌
	- http 요청에서는 80포트가 기본(이라서 우리가 평소에 :80 안하는 것)
  <img src="https://user-images.githubusercontent.com/89369520/130972810-9ed62f81-5071-4c4a-9027-9546ab4c5c4d.png" height="200">

### +) mongoDB 개인설정
#### +mongoDB 접속 계정 생성하기
1. 우리가 만든 mongoDB를 외부에 열어주기 전에, 접속에 필요한 아이디와 비밀번호를 세팅해봅시다! (설정 안하면 누구나 DB정보를 볼 수 있다는..!)
```bash
    mongo
```

2. 좌측에 '>' 표시가 나오면 성공적으로 MongoDB에 접속한 것입니다! 다음 명령어를 순차적으로 입력해주세요. 눈치 채셨겠지만, test, test 자리에 내가 넣고 싶은 아이디/비밀번호를 넣으면 됩니다. (영어로..!)
```bash
# admin으로 계정 바꾸기
use admin;

# 계정 생성하기
db.createUser({user: "test", pwd: "test", roles:["root"]});
```
3. 아래와 같은 화면을 보면 완성!
<img src="https://user-images.githubusercontent.com/89369520/130973398-b364229f-442f-4698-87a9-0473a94c1d08.png" height="70">

``` bash
# 나오기
exit
# MongoDB 재시작
sudo service mongod restart
```

#### +mongoDB를 외부에 열어주기
1. mongoDB는 디폴트로 내부에서만 접속을 허용하고 있습니다. 이 작업은 외부에서 접근이 가능하도록 잠금을 풀어주는 것입니다. 리눅스 자체 에디터(고급 메모장 정도로 생각!)인 Vim이 등장합니다.
`a` 를 눌러야 입력 모드가 되고, `:wq` 를 눌러야 저장하고 나올 수 있습니다.
```bash
sudo vi /etc/mongod.conf

# sudo: 관리자(SuperUser) 권한으로 다음을 실행
# => "관리자 권한으로 /etc 폴더 아래 mongod.conf 파일을 Vim으로 켜줘!"라는 뜻입니다
```
2. 위 명령어를 실행하신 후, 아래 방향 화살 키를 누르시면 다음과 같은 내용이 보입니다.
<img src="https://user-images.githubusercontent.com/89369520/130973726-3db26983-deb8-4e3b-94de-1494675770a0.png" height="200">

```bash
# 입력 모드 전환
i
```

3. 위 붉은 박스의 내용을 아래와 같이 바꿔주세요!
<img src="https://user-images.githubusercontent.com/89369520/130973916-1016f758-c379-47f2-8e42-e03025cbd366.png" height="200">

```bash
# 내용 저장하고 에디터 종료하기. esc 누르고 다음 입력.
:wq

# 재시작
sudo service mongod restart
```

## 14. Filezilla로 서버에 업로드, 브라우저에서 접속하기 (+Robo3T)
### 25) Robo3T create / Filezilla / pymongo 설치 / 브라우저 접속
- Robo3T로 내PC → 서버DB 접속하기 (와 정신 나갈뻔)
Robo3T → create → mongoDB connections 세팅(id, pw)
- 기존 코드 아래와 같이 수정 후에,
```python
client = MongoClient('localhost', 27017)
-> 변경하기
client = MongoClient('mongodb://id:pw@localhost', 27017)
```
- Filezilla 드래그앤드롭 복사
- terminal에서 pymongo 설치 후,
브라우저에서 접속 → http://내AWS아이피:5000/
```bash
# 설치
pip install pymongo

# 실행
python app.py
```

## 16. nohup 설정하기
### 31) SSH 접속을 끊어도 서버가 계속 돌게 하기
- Terminal 종료시 (=즉, SSH 접속을 끊으면) 프로세스가 종료되면서, 서버가 꺼짐.
<br> 원격접속을 끊어도, 서버는 계속 동작하게 하자.
```bash
# 원격 접속을 종료하더라도 서버가 계속 돌아가게 하기
nohup python app.py &

# 서버 강제종료 : 아래 명령어로 미리 pid 값(프로세스 번호)을 본다
ps -ef | grep 'app.py'
# 아래 명령어로 특정 프로세스를 죽인다
kill -9 [pid값]

# 다시 켜기
nohup python app.py &
```
```
표준 방법을 사용해서 시스템의 모든 프로세스를 보려면,
ps -e
ps -ef
ps -eF
ps -ely

-e : 모든 프로세스(-A와 같다)
-f : full format으로 보여준다(자세히 보여준다)
-F : 더 자세히 보여준다
-l : long format으로 보여준다는데 그다지 좋지 않아보인다(좀 잘리는듯-_-)
-y : flag를 안보여준다. -l 옵션하고만 사용할 수 있다고 한다;
```

## 17. 도메인 구입 & 연결
### 33) 도메인 구입 & 연결
- 도메인을 구입한다?
<br> - 네임서버를 운영해주는 업체에 IP와 도메인 매칭 유지비를 지불하는 것
- 과정 : [가비아 접속](https://my.gabia.com/service#/) → DNS관리툴 → 도메인 연결 → 호스트 이름, IP 주소 입력

## 18. og 태그
### 37) og 태그 만들기
- static 폴더 하위에 이미지 파일 / 
<br> 프로젝트 HTML의 <head>~</head> 사이에 작성
<img src="https://user-images.githubusercontent.com/89369520/130974449-491f479f-ad97-4a02-bb15-1e6ce6281343.png" height="200">
1. "내 사이트의 제목" 입력하기
2. "보고 있는 페이지의 내용 요약" 입력하기
3. 적당한 이미지를 만들거나/골라서 static폴더에 ogimage.png로 저장하기!
(사이즈 800x400인 이미지를 구글에서 검색!)

```jsx
<meta property="og:title" content="Trip to JPN" />
<meta property="og:description" content="OSAKA" />
<meta property="og:image" content="{{ url_for('static', filename='ogimage.png') }}" />
```

- 이미지를 바꿨는데 이전 ogimage가 그대로 나온다?
<br> → 페이스북/카카오톡 등에서 처음 것을 한동안 저장해놓기 때문.
<br> - 페이스북 og 태그 초기화 하기: [https://developers.facebook.com/tools/debug/](https://developers.facebook.com/tools/debug/)
<br> - 카카오톡 og 태그 초기화 하기: [https://developers.kakao.com/tool/clear/og](https://developers.kakao.com/tool/clear/og)

> **🎉 와! 수료를 축하합니다!!🎉**
<br> 이로써 5주 간의 모든 수업이 끝났습니다. 의미있고 뿌듯했던 5주로 기억되길 진심으로 바랍니다.
