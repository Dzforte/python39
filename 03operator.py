
# 파이썬 자료형 - 정수, 실수, 문자, 불 #
# 정수 자료형 - 소수점이하의 값이 없는 수 #

int1 = 123
int2 = 0b1001001001010   # 2진수
int3 = 0o54  # 8진수
int4 = 0x7F5D  # 16진수


# 2/8/16 진수로 출력는 print함수 사용시 10진수로 출력
print(int3)

# 2/8/16 진수로 출력하려면 bin, oct, hex 함수 등을 이용함
print(int2, bin(int2))
print(int2, oct(int2))
print(int2, hex(int2))


# 문자 자료형
# 긴 문장은 여러줄로 나눠 작성
str1 = "내려갈 때 \
보았네 \
올라갈 때 못 본 \
그 꽃"

print(str1)

# 화면 출력시 줄바꿈 표시
str2 = """
내려갈 때 보았네
올라갈 때 못 본 그 꽃
"""

print(str2)


# 문자열 슬라이싱 slicing
# 문자열은 각각의 문자들로 구성되어 있음
# 인덱스를 통해 개별 문자에 접근 가능
# 또한, : 를 이용해서 부분문자열 참조 가능


str3 = 'hello world!!'

print(str1[0])
print(str3[7])    # 왼 -> 오
print(str3[-7])   # 오 -> 왼


print(str3[0:5])  # 변수명[시작:끝-1]
print(str3[:5])   # 생략 가능

print(str3[-7:])


# len 함수 사용시 문자열의 길이 출력
len(str3)


# 부울 자료형 - 참/거짓을 나타내는 자료
# True, False 등으로 표현
# 숫자가 0이거나 빈 문자열이면 False로 표현


# 수식 expression
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 => 피연산자와 연산자로 구성됨.

#대입식 : 대입연산자를 이용한 수식 (변수 = 수식)
a = 10; b = 20; c= 30
print(a,b,c)

x,y,z = 10, 20, 30
print(x, y, z)

# 산술식 : 산술연산자를 이용한 수식
# 파이썬에서는 //, %, ** 도 지원

print(10/3, 10 % 3, 10 // 3)  # 나누기, 나머지, 몫

print(10**1, 10**2, 10**3)  # 지수 연산

# 관계식 : 관계연산자(대소, 순서 관계) 를 이용한 수식

print(10>3, 10<3)


# 논리식 : 논리연산자(논리 합/곱/부정)를 이용한 수식
# 또한, 둘 이상의 논리식이나 관계식
# 논리식의 경우 수식의 구성에 따라 단축식 평가 short-circuit가 가능

print((5 == 3) and (5 > 3))
print((5 == 3) or (5 > 3))

# and 연산시 첫번째 수식의 결과가 F면 단축식 평가 적용
print(3 > 5 and 2 < 3)

# 변수 = 변수 + 수식 => 변수 += 수식

# 연산자 우선순위
# 괄호내 연산자 -> 단항연산자 -> 산술연산자 -> 관계연산자 -> 논리연산자


# 연산자의 부수적인 기능 - 문자열 연산
# + : 문자열 연결
# * : 문자열 반복할 때 씀

str1 = 'hello'
str2 = 'World'
print(str1+str2)

print(str1 * 3)

print(8*str2)


# 숫자형과 문자형의 논리 연산
# 0 또는 빈 ㅁ누자열은 false로 인식
# bool 함수를 이용하면 지정한 값의 논리값을 알 수 있음
print( bool(0), bool(''))

# 다음 수식의 결과는 True인 값이 출력
print(0 and 'abc', 1 and 'abc')
print('' or 'abc', '' and 'abc')


#
print('123'+'456')
print(123+int("456"))