# print 함수
# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 출력함

name = '김철수'
kor = 99
eng = 98
mat = 99
total = kor + eng + mat
avg = (kor + eng + mat) / 3

print('이름 :', name)
print('국어 :', kor, '영어 :', eng, '수학 :', mat)
print('총점 :', total)


# 출력 서식 사용 : % 문자 사용
# print(출력 서식 % 변수들...)
# 출력서식 문자 : %d, %f, %s
print('이름 : %s' %name)

print('국어 : %d 영어 : %d 수학 : %d' % (kor, eng, mat))
print('국어 : %3d 영어 : %3d 수학 : %3d' % (kor, eng, mat))
print('국어 : %03d 영어 : %03d 수학 : %03d' % (kor, eng, mat))

print('총점 : %d, 평균 : %.1f' % (total, avg))


# 출력 4 - 인덱스, 출력서식 사용 : .format함수 사용

# print({인덱스(출력순서):출력서식}.format(변수들...))

print('이름 : {0:s}'.format(name))


# 출력 5 - 문자열 템플릿 (f-string) : py3.6 이후 지원 (추천!!)
## print(f'{변수명:출력서식})

print(f'이름 : {name:s}'  f' 국어 : {kor:d}')

# % 서식
gugu = 7
print('7 X 1 = %s' % gugu)

# .format
print('7 X 1 = %s' % gugu)
print('7 X 1 = {0:d}'.format(gugu))

# f-string
print(f'7 X 1 = {gugu:d}')
print(f'7 X 1 = {gugu:2d}')