# 33 - 신용카드 판별

cardNum = (input('카드번호 6자리를 입력하세요'))
cardNum1 = int(cardNum)

if 100000 <= cardNum1 <= 999999 :
    if cardNum[:2] == '35':
        if cardNum[2:6] == '6317':
            print('NH농협카드')
        elif cardNum[2:6] == '6901':
            print('신한카드')
        elif cardNum[2:6] == '6912':
            print('KB국민카드')
        else:
            print('잘못된 카드 번호입니다. ')
    elif cardNum[0] == '4':
        if cardNum[1:6] == '04825':
            print('비씨카드')
        elif cardNum[1:6] == '38676':
            print('신한카드')
        elif cardNum[1:6] == '57973':
            print('국민카드')
        else:
            print('잘못된 카드 번호입니다. ')
    elif cardNum[0] == '5':
        if cardNum[1:6] == '15594':
            print('신한카드')
        elif cardNum[1:6] == '24353':
            print('외환카드')
        elif cardNum[1:6] == '40926':
            print('국민카드')
        else:
            print('잘못된 카드 번호입니다. ')
    else:
        print('잘못된 카드 번호입니다. ')

else:
    print('카드 번호가 잘못되었습니다.')

## switch ~ case 와 비슷하게 작성해보기
# 파이썬은 지금까지 (~v3.9) switch ~ case 구문을 지원하지 않음
# 만일, switch ~ case 구문을 구현하려면 dict를 이용해야하마
# 3.10 부터는 match case 라는 구문으로 구현가능

# dict 자료구조
# 키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류임
# 객체명 = {키:값} -> 객체명.get(키), 객체명[키]

cards = {'356317':'NH농협카드', '404825':'비씨카드'}
print(cards.get('404825'))




name = input('이름')
kor = int(input('국어'))
mat = int(input('수학'))
eng = int(input('영어'))
tot = kor + mat + eng
avg = tot/3

grade = {10:'수',
         9:'수',
         8:'우',
         7:'미',
         6:'양',
         5:'가',
         4:'가',
         3:'가',
         2:'가',
         1:'가'
         }

print(grade.get(avg//10))

# 3항 연산자 - if 단축문 : 컴프리헨션
# 참일 떄 값 if 조건식 else 거짓일때 값

print('참' if True else '거짓')

# ex) 윤년여부를 출력하는 프로그램을 작성하시오
# 단, 3항 연산자를 이용해서 구현함

year = int(input("연도를 입력하세요"))

# print(year, '는 윤년입니다.') if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else print (year, '는 평년입니다.')


year = int(input("연도를 입력하세요"))
isLeapYear = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
result = '윤년입니다.' if isLeapYear else '평년입니다.'
print(year, result)


## ex) 년도와 월을 입력받아
# 윤년여부와 입력한 달의 마지막 날을 출력하는 프로그램을 작성하세요.


year = int(input("연도를 입력하세요"))
isLeapYear = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
result = '윤년입니다.' if isLeapYear else '평년입니다.'
#
# isLeapYear = {' : '
#          }
print(f'{year} 년도는 {result} 입니다. {year} 년도의 {month}월은 {day.get(result)}까지 있습니다. ')


