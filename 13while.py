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

print(main_menu)
input('=> 작업을 선택하세요 ')