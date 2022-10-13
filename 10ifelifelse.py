# if~else만으로 다양한 조건을 판단하기 어려움
# 다양한 조건에 따라 판단하기 위해서는
# if ~ elif ~ else 구문을 사용해야 함
# -> 물론 여러개의 if문을 사용해서 처리 가능함

# if 조건식1:
#    조건식1이 참일때 실행할 문장
# elif 조건식2:
#    조건식2이 참일때 실행할 문장
# ...
# else:
#    거짓일때 실행할 문장


# 결과 조건 : 점수 0 ~ 50 : 노력하세요
#                 51 ~ 80 : 잘했어요.
#                 81 ~ 100 : 최고예요!

score = int(input('점수를 입력하세요'))

if 0 < score <= 50 :
    print('노력하세요')
elif 50 < score <= 80 :
    print('잘했어요')
elif 80 < score <= 100 :
    print('최고예요!')
else :
    print('잘못 입력하셨어요...')


# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 계산하고 출력함
# 학점 처리 조건은 수우미양가로 함

kor = int(input('국어는?'))
eng = int(input('수학은?'))
mat = int(input('영어는?'))

tot = kor + eng + mat
avg = (kor + eng + mat) / 3

if 90 <= avg <=100:
    print('수')
elif 80 <= avg <90:
    print('우')
elif 70 <= avg <90:
    print('미')
elif 60 <= avg <90:
    print('양')
elif avg <60:
    print('가')
else :
    print('성적을 잘못 입력하셨습니다.')


# 수수료 계산
weight = int(input('짐의 무게는 얼마입니까'))
charge = (weight//10)*10000
if charge == 0 :
    print('수수료는 없습니다.')
else :
    print(f'수수료는 {charge}원 입니다.')


# 출생년도를 입력받아 나이 계산한 후 
# 나이에 따른 학생 분류 후 결과 출력
# ~ 8 : 미취학 아동
# ~ 14 : 초등학생
# ~ 17 : 중학생
# ~ 20 : 고등학생
# ~ 26 : 대학생
# 26 ~ : 학생이 아닙니다.

birthYear = int(input())
birthYear = 2022 - birthYear + 1

if birthYear < 8:
    student = '미취학 아동'
elif 8 <= birthYear < 14:
    student = '초등학생'
elif 14 <= birthYear < 17:
    student = '중학생'
elif 17 <= birthYear < 20:
    student = '고등학생'
elif 20 <= birthYear < 26:
    student = '대학생'
else :
    student = '학생이 아닙니다.'
print(student)