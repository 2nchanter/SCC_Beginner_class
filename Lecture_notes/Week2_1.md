## 01. 2주차.
- jQuery, Ajax
<br> HTML 받았다고 가정하고, JS로 다시 서버에 데이터를 요청하고 받아보자.
<br> jQuery를 이용, JS로 HTML을 쉽제 제어하고, Ajax를 이용, 다시 서버에 데이터를 요청하고 받아보자.

## 02. Javascript 복습
### 1) Javascript 복습 - 짝/홀수에 따라 alert, onclick 함수
```css
<script>
   let count = 1;
      function hey() {
         if (count % 2 == 0) {
            alert('짝수입니다')
         }
         else {
            alert('홀수입니다')
         }
         count += 1; // count = count + 1;
      }
</script>
 ```
- onclick="hey()" : 클릭시 hey 함수를 불러라
- function 안에서 변수를 선언해서 사용하면, 함수 끝나면 사라진다. (숫자 누적 x)
<br> 바깥에 두고 전역변수로 사용하자.
- jQuery로 btn의 컬러나, div 박스를 감춰보자.

## 04. JQuery 다뤄보기
### 4) jQuery?
 - 소프트웨어가 아니라, 미리 작성된 JS 코드, 보다 직관적으로 짧게 작성 가능 (임포트 후 사용가능)
 - css 선택자 - class / jQuery 선택자 - id
 
### 5) 자주쓰는 jQuery들 다뤄보기
- code
```jsx
// 크롬 개발자도구 콘솔창에서 쳐보기
$('#post-url').val(); // val : input box에 사용
// id 값이 post-url인 곳을 가리키고, val()로 값을 가져온다.

$('#post-box').hide(); // 박스 숨김
$('#post-box').show(); // 박스 나타냄

$('#post-box').css('width','700px'); // '동적'으로 커지게 가능.
$('#post-box').css('display'); // display 상태값 : block, none(있는데 안보임)

$('btn-posting-box').text('hi'); // text 변경

let temp_html = '<button>나는 추가될 버튼이다!</button>';
$('#cards-box').append(temp_html); // 버튼 넣기

// backtick을 사용하면 문자 중간에 Javascript 변수를 삽입할 수 있음.
const num1 = 10;
const num2 = 20;
console.log(num1 + ' + ' + num2 + ' = ' + (num1+num2) +  " 입니다.");
console.log(`${num1} + ${num2} = ${num1+num2} 입니다.`);
```

## 05. JQuery 적용하기
### 6) 포스팅박스 열기/닫기, 버튼 바꾸기
- console.log 가 '콘솔'창에 찍어주는 거였다니,,ㅎㅎ
- display: none 하면 처음부터 닫아주는 거였다니,,ㅎㅎ
- code
```jsx
<script>
   function openclose() {
      let status = $('#post-box').css('display');
      if (status == 'block') {
         $('#post-box').hide();
         $('#btn-posting-box').text('포스팅박스 열기')
      } else {
         $('#post-box').show();
         $('#btn-posting-box').text('포스팅박스 닫기')
      }
   }
</script>
```

## 06. Quiz_JQuery 연습하기
### 7) jQuery, JS ?
- jQuery가 JS보다 몇줄 안쓰고도 기능 구현이 가능하다. 따라서 개발 속도는 빨라진다. 하지만 jQuery는 JS로 만들었기 때문에 처리 속도는 느리다. 이걸 pc가 보완해줄 뿐이다.
-> 결론 : 평상시 jQuery를 즐겨 쓰되, 빠른 처리속도가 필요할때 JS를 섞자.
- code : [frontend_prac/practice.html](https://github.com/2nchanter/SCC_Beginner_class/blob/main/frontend_prac/practice.html)

- Q. let 이게 왜 안되지?;;
<br> 2, 3번째 let은 .split이 될 때는 값이 들어가지만, 안 될때는 값이 없어서 에러를 띄우게 된다.
<br> if문 사용하여 에러 띄울때, 분류되는 걸 잘 생각하자.
<img src="https://user-images.githubusercontent.com/89369520/130961497-7b59c617-0b0a-4a81-b9fb-81175918451b.png" height="200">

```python
function q2() {
   let email = $('#input-q2').val();
   let result1 = email.split('@')[1]
   let result2 = result1.split('.')[0]
   if (email.includes('@')) {
      alert(result2);
   } else {
      alert('이메일이 아닙니다!');
   }
}
```
