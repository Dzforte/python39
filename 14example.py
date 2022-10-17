# 78 ex) 숫자 맞추기 (1~10)
import random as rnd

rnd.seed(13498045982)

com = rnd.randint(1, 10)
print('>> 숫자 맞추기 게임 <<')

while True:
    my = int(input('숫자를 넣으세요'))
    if com == my:
        print('정답!!')
        break
    else:
        print('틀렸습니다...')

# ex) 복권 프로그램 - 3자리수 난수 생성/사용자 입력
# 난수 범위 - 100 ~ 999, 위치는 상관 없이 숫자만 일치 여부 판단
# ex) 123 -> 345(1), 317(2), 312(3)
# 문자열 슬라이싱을 위한 문자열 변환 str 함수 사용

# 3개 일치 - 상금 백만원!
# 2개 일치 - 상금 5만원!
# 1개 일치 - 상금 1만원!
# 0개 일치 - 다음 기회에!

import random as rnd

seednum = int(input('시드 넘버를 입력해주세요'))

rnd.seed(seednum)
com = rnd.randint(100, 999)
com1 = str(com)
result = 0

while True:
    my = input('세자리 번호를 입력하세요')
    if int(my) < 100 or int(my) > 1000:
        print('세자리 숫자를 입력해주세요.')
    else:
        for i in range(3):
            for j in range(3):
                if com1[i] == my[j]:
                    result += 1
        if result == 0:
            print('다음 기회에!')
        elif result == 1:
            print('상금 1만원')
        elif result == 2:
            print('상금 5만원')
        elif result == 3:
            print('상금 100만원')
    result = 0
