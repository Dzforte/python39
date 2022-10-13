


#26

salary = int(input(" 연봉을 입력하세요 "))
isMarried = input(" 결혼 여부를 입력하세요. 기혼 : Y  |  미혼 : N ")

if isMarried == 'Y' or 'y':
    if salary < 3000:
        print(f'납부하실 세금은 {salary*0.1:.0f} 만원입니다.')
    else:
        print(f'납부하실 세금은 {salary*0.25:.0f} 만원입니다.')
elif isMarried == 'N' or 'n':
    if salary < 6000:
        print(f'납부하실 세금은 {salary*0.15:.0f} 만원입니다.')
    else:
        print(f'납부하실 세금은 {salary*0.35:.0f} 만원입니다.')
else:
    print('잘못 누르셨습니다...')



#25 - 복권 발행 프로그램 v1
# 난수 생성시 random 모듈의 randrange(범위) - randrange(start, ed-1)

import random as rnd

usernum1 = int(input("첫번째 번호 입력하세요"))
usernum2 = int(input("두번째 번호 입력하세요"))
usernum3 = int(input("세번째 번호 입력하세요"))

lottokey = rnd.randrange(1, 10)
print(lottokey)

if usernum1 == lottokey or usernum2 == lottokey or usernum3 == lottokey:
    print("당첨입니다!!")
else:
    print("꽝!")



#27

year = int(input("연도를 입력하세요"))

if year % 4 == 0 and year % 100 != 0:
    print(f'{year}년은 윤년입니다.')
elif year % 4 == 0 and year % 400 == 0:
    print(f'{year}년은 윤년입니다.')
else:
    print(f'{year}년은 평년입니다.')



#28

number = 30
if number % 2 == 0:
    print('입력한 값은 짝수입니다.')
else: print('입력한 값은 홀수입니다.')

