# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장, 조회, 수정, 삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

# 성적프로그램 v2
# 이름,국어,영어,수학을 입력하면
# 총점,평균,학점을 처리해서 결과출력
# 단, 3명의 학생에 대해 성적처리를 진행함
# 성적 자료 초기화

# name1, name2, name3 = '혜교', '지현', '수지'
# kor1, kor2, kor3 = 99, 65, 75
# 처리할 데이터 갯수에 따라 변수도 증가해야 함


# p110, 1

lst = [10, 1, 5, 2]
for i in range(len(lst)):
    lst.append(int(lst[i]))
print(lst)


lst = [10, 1, 5, 2]
for i in range(len(lst)):
    lst.append(int(lst[i]))
lst.append(lst[0]*2)
print(lst)


lst = [10, 1, 5, 2]
for i in range(len(lst)):
    lst.append(int(lst[i*2-1]))
print(lst)


# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근(참조)하려면 변수[인덱스] 형식을 사용

menus = ['라면', '돈까스', '짜장면', '냉면', '정식']
print(menus)

# 리스트에서 일부 요소만 출력
print(menus[2])

# 리스트에서 모든 요소 출력
# print(menus[0], menus[2].....)
# 번거로우니까 반복문으로 출력

for i in range(len(menus)) :    #len(대상)의 요소 갯수를 알려줌
    print(menus[i], end= ' ')

# 다른 방법
# for i in 객체:
for i in menus:
    print(i, end=' ')

# 동적으로 리스트 생성하기
menus1 = []    # 빈 리스트 선언

# 리스트에 요소를 추가하려면 append 함수 사용
menus1.append('라면')
menus1.append('돈까스')
menus1.append('짜장면')
menus1.append('우동')
menus1.append('백반')

print(menus1)

# append 한 요소는 리스트의 맨 뒤에 부착

# 지정한 위치에 새로운 요소 추가 : insert(인덱스, 값) ; 값이 들어가고 원래 있던 값을 뒤로 하나씩 밀게 됨.
menus1.insert(2,'냉면')
print(menus1)

# 리스트 요소의 값 수정 : 객체명[인덱스] = 새로운 값

menus1[2] = '울면'
print(menus1)

# 리스트 요소 삭제
menus1.remove('울면')

# 리스트 요소 삭제 : pop(인덱스) - 위치로 삭제
menus1.pop(1)

# 리스트 요소 삭제 : pop() - 위치로 삭제 + 뒤에서부터 삭제
menus1.pop()

# 리스트로 다양한 데이터 다루기

datas = []

datas.append(1)
datas.append(2.5)
datas.append(True)
datas.append('hello')
datas.append([1,3,5])

print(datas)



