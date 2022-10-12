
#1
print('*   *    **    ****    ****   *   *    /////')
print('*   *   *  *   *   *   *   *  *   *   | o o |')
print('*****  *    *  ****    ****    * *   (|  ^  |)')
print('*   *  ******  *   *   *   *    *     | [_] |')
print('*   *  *    *  *    *  *    *   *      ----- ')



# 논리식과 산술식(값)이 결합된 수식에서는
# 논리식의 결과가 True면 값이 출력
# 논리식의 결과가 False면 False가 출력
print((3>4) and 5/8)

print(23/5 + 23/5.0)

# print(2.0 + 'a')
# print('a' + 'b')

print('a' and not 'b')

c = 0x16 + 0x08

print( c )

#11

name = '홍길동'
weight = '55.5'
age = 35

print(name, weight, age)


# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#         만나이(출생시 0살, 생일이 지나면 + 1)
#         연나이(현재연도 - 출생연도)
birthYear = 1990
currentYear = 2022
isPassBirth = True

age = currentYear - birthYear

print('연나이', age)
print('세는 나이', 1 + age)
print('만나이', )


# 파이썬의 if 단축식 : 참일 때 값 if 조건식 else 거짓일 떄 값

print('만나이', (age + 1) if isPassBirth else age)



#13 구구단 7단

print('7 X 1 =', (7*1))


print("★ 구구단을 출력합니다.\n")
for x in range(2, 10):
    print("------- [" + str(x) + "단] -------")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("---------------------")