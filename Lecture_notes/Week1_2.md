## 12. Javascript 맛보기
### 21) JS?
- 프로그래밍 언어 중 하나로, 브라우저가 알아들을 수 있는 언어.
<br> : 코드를 수려하게 짜는것보다 동작하게 짜는 것이 중요하다.
<br> 어떻게 하면 깨끗하게 짤 수 있는지, 왜 깨끗하게 짜야 하는지.
<br> 필요성에 의해 인식하면서 단계단계 건너가보자.
<br> `개발자 도구 - console창에서 function 바로바로 확인하자.`

### 23) JS 사용해보기
- `<head> ~ </head>` 안에 `<script> ~ </script>` 로 공간을 만들어 작성
- HTML 연결. 버튼을 클릭하면 경고창이 띄우기
```jsx
<script>	
   function hey(){
   alert('안녕!');
   }
</script>
```
```html
<button onclick="hey()" type="button" class="btn btn-primary">기사저장</button>
```

## 13. Javascript 기초 문법 배우기(1)
### 24) 변수, 기본연산, list, dict, split, join
- 왜 중요하지?
<br> 순서를 표시할 수 있고, 정보를 묶을 수 있어서.
```
   # 앞에서 언급한 <스파르타과일가게>가 정말 잘 되어서 전국에서 손님이 찾아오고 있습니다.
   # 대기표를 작성하기 위해서 온 순서대로 이름, 휴대폰 번호를 적도록 하였는데요. 변수만을 사용한 모습은 다음과 같습니다.
   let customer_1_name = '김스파';
   let customer_1_phone = '010-1234-1234';
   let customer_2_name = '박르탄';
   let customer_2_phone = '010-4321-4321';
   ...(알아보기 힘듭니다.)
   
   # 딕셔너리를 활용한다면 다음과 같이 고객 별로 정보를 묶을 수 있습니다.
   let customer_1 = {'name': '김스파', 'phone': '010-1234-1234'};
   let customer_2 = {'name': '박르탄', 'phone': '010-4321-4321'};

   # 그리고 순서를 나타내기 위해 리스트를 사용하면, 이렇게나 깔끔해집니다.
   let customer = [
      {'name': '김스파', 'phone': '010-1234-1234'},
      {'name': '박르탄', 'phone': '010-4321-4321'}
   ]
   # 보기에도 깔끔해지고, 다루기도 쉬워지고, 고객이 새로 한 명 더 오더라도 .push 함수를 이용해 간단하게 대응할 수 있습니다.
```

- "마우스 오른쪽 클릭 → 검사 → console"
console.log(변수) : 콘솔 창에 괄호 안의 값을 출력
- 왜 let을 안써도 되는데 쓰는걸까?
c-family language는 block-level scope인데, Javascript는 function-level scope 이므로, 전역변수가 중복되는 혼란을 줄이기 위해 'let'을 써서 bls로 만들어줌으로 중복을 피한다.

#### 변수, 기본연산
```jsx
let num = 20
num = 'Bob'
// 변수는 값을 저장하는 박스
// 한 번 선언했으면, 다시 선언하지 않고 값을 넣음

let a = 1
let b = 2
a+b // 3
a/b // 0.5
let first_N = 'Bob' // snake case 변수선언방식
let lastN = 'Lee'. // camel case 변수선언방식
first_N+lastN // 'BobLee'
first_N+' '+lastN // 'Bob Lee'
first_N+a // Bob1 -> 문자+숫자를 하면, 숫자를 문자로 바꾼 뒤 수행합니다.
```
#### list, dict
```jsx
// list : 순서를 가지고 있는 형태
let b_list = [1,2,'hey',3] // 선언, 순서는 0, 1, 2, 3
b_list.push('헤이') // 리스트에 요소 넣기
b_list // [1, 2, "hey", 3, "헤이"]
b_list.length // 리스트의 길이 구하기, 5를 출력

// dict : key-value 값의 묶음
let b_dict = {'name':'Bob','age':21} // 선언
b_dict['name'] // key 값 input, 'Bob'을 출력
b_dict['height'] = 180 // 딕셔너리에 키:밸류 넣기
b_dict // {name: "Bob", age: 21, height: 180}을 출력

// list (dict)
names = [{'name':'bob','age':20},{'name':'carry','age':38}]
// names[1]['name']의 값은? 'carry'
new_name = {'name':'john','age':7}
names.push(new_name)
// names의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
// names[2]['name']의 값은? 'john'
```
#### split, join
```jsx
// split
let txt = '서울시-마포구-망원동'
let names = txt.split('-'); // ['서울시','마포구','망원동']
// merge
let result = names.join('>'); // '서울시>마포구>망원동'
```

## **14. Javascript 기초 문법 배우기(2)**
### 25) 함수, 조건문, 반복문
#### 함수
```jsx
// 만들기
function 함수이름(필요한 변수들) {
내릴 명령들을 순차적으로 작성
}
// 사용하기
함수이름(필요한 변수들);

// 두 숫자를 입력받으면 더한 결과를 돌려주는 함수
function sum(num1, num2) {
console.log('num1: ', num1, ', num2: ', num2);
return num1 + num2;
}

sum(3, 5); // 8
sum(4, -1); // 3
```
#### 조건문 : and &&, or ||, equal ==
```jsx
// AND 조건은 이렇게
function is_adult(age, sex){
   if(age > 20 && sex == '여'){
      alert('성인 여성')
   } else if (age > 20 && sex == '남') {
      alert('성인 남성')
   } else {
      alert('청소년이에요')
   }
}

// 참고: OR 조건은 이렇게
function is_adult(age, sex){
   if (age > 65 || age < 10) {
      alert('탑승하실 수 없습니다')
   } else if(age > 20 && sex == '여'){
      alert('성인 여성')
   } else if (age > 20 && sex == '남') {
      alert('성인 남성')
   } else {
      alert('청소년이에요')
   }
}

is_adult(25,'남')
```
#### 반복문 : i=0이고, i가 100보다 작을때까지 더해가면? (0~99 출력시)
```jsx
for (let i = 0; i < 100; i++) {
console.log(i);
}

// 과정
for (1. 시작조건; 2. 반복조건; 3. 더하기) {
     4. 매번실행
}

1 -> 2체크하고 -> (괜찮으면) -> 4 -> 3
-> 2체크하고 -> (괜찮으면) -> 4 -> 3
와 같은 순서로 실행됩니다.
i가 증가하다가 반복조건에 맞지 않으면, 반복을 종료하고 빠져나옵니다.
```
#### 그러나 위처럼 숫자를 출력하기 보다, 주로 리스트와 함께 쓰인다.
```jsx
let people = ['철수','영희','민수','형준','기남','동희']

// 이렇게 하면 리스트의 모든 원소를 한번에 출력할 수 있겠죠?
// i가 1씩 증가하면서, people의 원소를 차례대로 불러올 수 있게 됩니다.
for (let i = 0 ; i < people.length ; i++) {
   console.log(people[i])
}

let scores = [
   {'name':'철수', 'score':90},
   {'name':'영희', 'score':85},
   {'name':'민수', 'score':70},
   {'name':'형준', 'score':50},
   {'name':'기남', 'score':68},
   {'name':'동희', 'score':30},
]

for (let i = 0 ; i < scores.length ; i++) {
      console.log(scores[i]);
}
// 이렇게 하면 리스트 내의 딕셔너리를 하나씩 출력할 수 있고,

for (let i = 0 ; i < scores.length ; i++) {
   if (scores[i]['score'] < 70) {
      console.log(scores[i]['name']);
   }
}
// 이렇게 하면 점수가 70점 미만인 사람들의 이름만 출력할 수도 있습니다.
```

## 16. 1주차 과제
### *) 기획서(레이아웃) 보기
<img src="https://user-images.githubusercontent.com/89369520/130957454-993ec7e4-be19-413e-b86f-d63bf671e21b.png" height="500">

- Code : [frontend_prac/01_HW.html](https://github.com/2nchanter/SCC_Beginner_class/blob/main/frontend_prac/01_HW.html)
