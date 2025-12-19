console.log('js 연결 확인')

//dom -> html 전체구조를 객체화 한 것
$(document).ready(
    function(){
        console.log('jquery 준비 완료');

        $("#btn").click(function(){     // .click 으로 바로 행동을 명령해도 되고,  $('#checkall').on('change',function(){}) 이것처럼 .on('change')  .on에 행동명령을 해도 됨
            $('#text').text('버튼클릭됨');
        })
        // 전체선택
        $('#checkall').on('change',function(){
            $('.chk').prop('checked',this.checked); // $('.chk').prop('checked',true); -> 로 하면 전체선택 풀어도 그대로 체크되어 있음
            // 개수를 카운트
            $('#count').text(checked)
        });
        //개별체크로 전체 컨트롤
        $('.chk').on('change',function(){       // .chk에서 .은 클래스 선택자라는 뜻
            const total = $('.chk').length
            const checked = $('.chk:checked').length     //const 고정시켜주기 위해서?
            $('#checkall').prop('checked',total == checked) //prop 상태를 말한다
            // 개수를 카운트
            $('#count').text(checked)
        
        });

        //선택 삭제
        $('#deleteBtn').click(function(){
            $('.tchk:checked').each(function(){ //each는 for 문이라고 생각하며 됨
                $(this).closest('tr').remove()     //this는 가장 가까운 명령을 행하라는 것 여기에서는 $('.tchk:checked')
            })
        });
        // 버튼 비활성화(중복 클릭 방지) 저장 결제 api 호출
        $('#saveBtn').click(function(){
            $(this).prop('disabled',true)

            setTimeout( ()=>{                       // function() 은 람다함수인 ()=> 과 동일
                $(this).prop('disabled',false)
            },1000);                                // 2000은 2초
        });
        // 입력값을 실시간 검증
        $('#username').on('input',function(){
            const val = $(this).val() //val  -> value
            if(val.length < 3){
                $('#msg').text('3자 이상 입력').css('color','red')  // .css 하면 바로 스타일 추가 가능
            }else{
                $('#msg').text('사용 가능').css('color','green')
            }
        });
        //동적 요소 추가
        let cnt = 1;
        $('#addBtn').click(function(){
            $('#list').append(      // cnt++ 는 cnt +=1 이랑 같은 뜻
                `   
                <div class = 'item'>
                    동적항목 ${cnt++}  
                    <span class = 'remove'>삭제</span>
                </div>
                `
            );
        })
// 이벤트 위임
// 이벤트 위임은 on 메소드로 사용
// 부모요소.on(이벤트종류, 자식요소선택자, 실행함수)
// javascript로 동적으로생성한 element는 javascript에서 해당요소의 이벤트를 감지 못함
// 왜냐하면 javascript 보다 나중에 생성된 element 이기 때문에
// html5는 이벤트 버블링이 있어서 모든 이벤트는 부모로 전파된다는 속성을 이용해서 역으로 
// 해당 부모가 이벤트를 감지해서 발생하면 자식의 부모 element를 제거할 수 있다
// 테이블, 리스트, 댓글
        $('#list').on('click','.remove',function(){
            $(this).parent().remove();
        })
    }
);