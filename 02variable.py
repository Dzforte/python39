# 변수
# 어떠한 값을 저장하는 장소를 기억하기 쉽게
# 문자형태로 나타낸 것
# 변수에 값이 저장되는 공간을 메모리라 함
# 변수에 값을 넣으라고 선언하면,
# 시스템상의 메모리 어딘가에 공간을 확보하고
# 그 공간의 실제주소와 이름을 매핑함

# 이름과 나이를 저장하는 변수 선언
name = "성춘향"
age = 99

# 변수에 저장된 값을 출력하려면 print 함수 사용
print(name, age)

# 여러 문장을 한줄에 표시하려면 ; 이용 (가독성 저하 - 비추)

name = '홍길동'; age = 90

# 변수명은 대소문자 구분

Name = '일지매'

print(name, Name)

#변수의 자료형을 알아보기 위해 type 함수 사용

print(type(name))

name = 123

print(type(name))




# ex) 회원정보 저장용 변수 선언

# 아이디, 비번, 이름, 나이, 이메일, 결혼여부, 통장잔액, 등록일

userid = "abc123"
passwd = "876xyz"
name = "abc123"
age = 35
email = "abc123@876xyz.com"
isMarried = True
hasMoney = 10000
regdate = "2022-10-11 14:39:15"
