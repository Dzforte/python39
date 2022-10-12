import math

# ex) 주민번호에서 생년과 월, 일, 성별을 추출해서 각 변수에 적절히 저장하세요

jumin = '202205092123456'
year = jumin[0:4]
month = jumin[4:6]
day = jumin[6:8]

if jumin[8] == '1':
    gender = '남성'
else:
    gender = '여성'

print(f'태어난 해 : {year:s}')
print(f'태어난 달 : {month:s}')
print(f'태어난 일 : {day:s}')
print(f'성별 : {gender:s}')

# 16 - 잔돈 계산기
# 비용과 지불 금액을 입력 받아 잔돈 계산

cost = int(input('지불금액을 입력하세요'))
pay = int(input('받은금액을 입력하세요.'))
change = cost - pay

a = math.trunc(change / 50000)
b = math.trunc(change % 50000 / 10000)
c = math.trunc(change % 50000 % 10000 / 5000)
d = math.trunc(change % 50000 % 10000 % 5000 / 1000)
e = math.trunc(change % 50000 % 10000 % 5000 % 1000 / 500)
f = math.trunc(change % 50000 % 10000 % 5000 % 1000 % 500 / 100)
g = math.trunc(change % 50000 % 10000 % 5000 % 1000 % 500 % 100 / 50)
h = math.trunc(change % 50000 % 10000 % 5000 % 1000 % 500 % 100 % 50 / 10)

# 정수 부분만 추출 하려면 '//'  ex) time = 12345678 ; day = time // 86400


print(f'''지불금액은 {cost:d} 원입니다.
받은금액은 {pay:d} 원입니다.
잔액은 {change:d} 원입니다.

50,000원권은 {a:d} 장 
10,000원권은 {b:d} 장
5,000원권은 {c:d} 장
1,000원권은 {d:d} 장
500원은 {e:d} 개
100원은 {f:d} 개
50원은 {g:d} 개
10원은 {h:d} 개
''')
