# 함수를 이용한 성적처리 프로그램

#함수 정의부

def displayMenu():
    main_menu = f'''
    성적 처리 프로그램 v1
    -----------------------
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    -----------------------'''
    print(main_menu)

def addSungJuk():
    name = input('이름은?')
    kor = int(input('국어는?'))
    eng = int(input('영어은?'))
    mat = int(input('수학은?'))

    tot = kor + eng + mat
    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    names = []
    kors = []
    engs = []
    mats = []
    tots = []
    avgs = []
    grds = []

    names.append(name)
    kors.append(kor)
    engs.append(eng)
    mats.append(mat)
    tots.append(tot)
    avgs.append(avg)
    grds.append(grd)

    input('성적 데이터 추가 완료!')


def readSungJuk():
    pass

def readOneSungJuk():
    pass


def modifySungJuk():
    pass


def removeSungJuk():
    pass

# 성적 데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부


while True:
    # 메뉴 표시 및 값 입력
    displayMenu()
    menu = input('=> 메뉴를 선택하세요 : ')

    if menu == '1': addSungJuk()
    elif menu == '2': readSungJuk()
    elif menu == '3': readOneSungJuk()
    elif menu == '4': modifySungJuk()
    elif menu == '5': removeSungJuk()
    elif menu == '0': break
    else: print('잘못된 번호를 입력했습니다!!')
