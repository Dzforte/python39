


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

#25

usernum1 = int(input("첫번째 번호 입력하세요"))
usernum2 = int(input("두번째 번호 입력하세요"))
usernum3 = int(input("세번째 번호 입력하세요"))

rnum1, rnum2, rnum3 = 1, 2, 3

if usernum1 == rnum1 and usernum2 == rnum2 and usernum3 == rnum3:
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

