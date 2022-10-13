
# for 반복변수 in range(시작값, 종료값-1, 증감값) : 반복실행할 문장

## range 함수 사용하기

# range(숫자) - 0 부터 숫자-1까지의 범위
print(list(range(10)))

# range(시작, 끝-1) - 시작값부터 끝값-1까지의 범위
print(list(range(1, 45+1)))

# range(시작, 끝-1, 증감값) - 시작값부터 끝값-1의 범위에 증감값을 포함시킴

print(list(range(1,10,2)))


# print 함수로 값 출력시 줄바꿈 문자가 자동 추가됨
# 줄바꿈 문자 대신 다른 문자로 대신하려면 end 속성을 사용
for i in range(1, 100+1):
    print(i, end=', ')

for i in range(1, 101):
    print(101-i, end=', ')

for i in range(1, 101, 2):
    print(i+1, end=', ')

# ex) 1 ~ 100까지의 정수들의 모든 합 계산 후 출력

result = 0
for i in range(1, 101) :
    result = result + i
print(result)


# 문자열에 반복문 적용하기
# ==> 문자열에서 문자를 하나씩 가져와서 출력함

for i in 'hello world':
    print(i, end=' ')


# ex) 단을 입력받아서 해당 단의 구구단을 출력

dan = int(input('숫자를 입력하세요'))
for i in range(1,10):
    print(f'{dan} X {i} = {dan*i}')

# ex) 3의 배수지만 2의 배수는 아닌 정수 출력하고
# 누적합도 계산해서 출력


result += i
print('수열 = ', end='')
for i in range (1, 100):
    if i%3==0 and i%2!=0:
        print(i, end= ',')
print()
print('누적합 = ', result)

