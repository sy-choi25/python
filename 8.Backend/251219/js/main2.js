console.log('js 연결 확인')

//dom -> html 전체구조를 객체화 한 것
$(document).ready(
    function(){
        //초기 렌더링 리스트업(READ)
        let users = [               //let 지역변수
            {id:1, name:'홍길동', email:'hong@test.com'},
            {id:2, name:'김철수', email:'kim@test.com'}
        ]
        //for user in users 파이썬에서 이거와 같음. 반복문
        users.forEach(user=>{
            $('#usertable').append(     // `` 이게 파이썬에서의 f'
                `
                <tr data-id="${user.id}">
                    <td><input type="checkbox" class="chk"></td>
                    <td>${user.id}</td>
                    <td>${user.name}</td>
                    <td>${user.email}</td>
                    <td>
                        <button class="edit">MODIFY</button>
                        <button class="remove">REMOVE</button>
                    </td>
                </tr>
                `            )
        });
        // 전체 선택 해제
        $('#checkall').on('change',function(){
            $('.chk').prop('checked',this.checked)
        });
        // 개별 선택. 동적 생성한 요소는 이벤트 위임으로 부모에게 이벤트를 위임해서 처리
        $('#usertable').on('change','.chk', function(){
            $('#checkall').prop('checked',
                $('.chk').length==$('.chk:checked').length
            )
        }); 
        // CREATE 행추가 prompt
        $('#addBtn').on('click',function(){
            const name = prompt('이름 입력');
            const email = prompt('이메일 입력');
            if(!name || !email) return;  // "만약(if) 이름이 없거나(!name) 또는(||) 이메일이 없으면(!email), 함수를 끝내라(return)."
            const newId = users.length? users[users.length-1].id+1 : 1 ; 
            check = age >= 19? '성인' : '미성년'; //3항 연산자

            // users[users.length-1].id+1 if user.length else 1 -> 파이썬 스타일
            
            // 자바스타일
            // if (users.length){
            //     const newId = users[users.length-1].id+1
            // }
            // else{
            //     const newId = 1
            // }
        });       

    }
);