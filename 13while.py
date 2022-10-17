# 수행 수가 일정하지 않다면 while, 수행 수가 일정하다면 for
count=1
while count <= 10:
    print('welcome!')
    count += 1
print('프로그램 종료!!!!!!')


num = 1
while num <= 100:
    print(f'{num}', end=' ')
    num += 1
print('끝')

# 홀수만 출력 (while)
num = 1
while num <= 100:
    print(f'{num}', end=' ')
    num += 2
print('끝')

# 홀수만 출력 (while)
num = 1
while num <= 100:
    print(f'{num}', end=' ')
    num += 2
print('끝')

# 모든 합 출력 (while)

num = 1
result = 0
while num <=100:
    num = num + 1
    result = result + num
print(result)



# 구구단 (while)
gugu = int(input('숫자를 입력하세요'))
num = 1
while num <=9:
    print(f'{gugu} X {num} = {gugu*num}')
    num += 1


# 3배수, 2배수 아닌 것
num = 1
result = 0
while num <= 100:
    if num % 3 == 0 and num % 2 != 0 :
       print(num, end=',')
    result = result + num
    num += 1
print(result)


# 무한루프
# 반복문의 조건식이 언제나 참이면
# 반복을 중단하지 않고 계속 반복을 지속하는 상황
# 단, 무한루프에서 탈출하려면 break를 이용
# while True:
# 반복실행할 문장

num = 1
result = 0
while True:
    if num <= 100: result += num
    else: break
    num += 1
print(num)
print(result)



# 1~1000 사이의 모든 정수의 합을 출력하세요, 단 누적합이 15000을 넘으면 반복문을 중지하고 결과를 출력

num1 = 0
result1 = 0
while True:
    if result1 < 15000:
        result1 += num1
        num1+=1
    else:
        break
print(num1)
print(result1)

#

#print(main_menu)
#input('=> 작업을 선택하세요 ')

# 성적처리 프로그램 메뉴화면 구현
# while문과 break 사용
main_menu = f'''
성적 처리 프로그램 v1
-----------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
-----------------------'''

while True:
    print(main_menu)
    menu = input('---> 작업을 선택하세요 : ')

    if menu == '0':
        print('성적 프로그램을 종료합니다.!')
        break
    elif menu == '1': print('성적 데이터 추가 완료!')
    elif menu == '2': print('성적 데이터 조회 완료!')
    elif menu == '3': print('성적 데이터 상세조회 완료!')
    elif menu == '4': print('성적 데이터 수정 완료!')
    elif menu == '5': print('성적 데이터 삭제 완료!')
    else: print('잘못된 번호를 입력하셨습니다...')



# 반복실행시 특정코드 회피 : continue
# 반복 실행을 유지하면서 특정 코드블럭의 실행을 생략하고 싶을 때 사용

# ex) 1~1000 사이의 모든 정수의 합을 출력하세요
# 단, 7의 배수나 9의 배수는 제외하고 누적합을 구함
i=0
hap=0
while  i <= 1000:
    i += 1
    if i % 7 == 0 or i % 9 == 0 : continue
    hap += i # 상황에 따라 실행될수도, 실행되지 않을 수도 있음
print(hap)

# ex4) 아이디, 비번을 입력받아서 일치하면 로그인 성공, 일치하지 않으면 로그인 실패
# 아이디: abc123, 비밀번호: 987xyz


while True:
    uid = input("아이디를 입력하세요")
    pwd = input("비밀번호를 입력하세요")
    if uid != 'abc123' and pwd != '987xyz':
        print('아이디 혹은 비밀번호가 잘못되었습니다.')
    else :
        print('로그인 성공!')
        break

# 난수 생성하기
# 파이썬에서 난수를 생성하려면 random 패키지 이용
# 생성방법 : 패키지.random.randint(시작값, 끝값)

import random as rnd

rnd.seed(22101)
for _ in range(6): # 반복 실행시 인덱스가 필요 없으면 _ 사용
    print(rnd.randint(1, 45), end=' ')

