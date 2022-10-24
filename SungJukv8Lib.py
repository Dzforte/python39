# oop를 이용한 성적처리 프로그램
# 성적 처리 프로그램의 함수들은
# sungjukv8lib, sungjukv8dao에 작성하고
# 모듈명은 sjv8로 줄여서 사용함

import csv
from SungJukv8Lib import SungJukv8Lib as sjv8

class SungJukv8Lib:
    sjs = []
    def displayMenu(self):
        main_menu = f'''
        성적 처리 프로그램 v6
        ----------------
        1. 성적 데이터 추가
        2. 성적 데이터 조회
        3. 성적 데이터 상세조회
        4. 성적 데이터 수정
        5. 성적 데이터 삭제
        0. 프로그램 종료
        ----------------'''
        print(main_menu)
        menu = input('메뉴를 입력하세요: ')

        return menu


    def input_sungjuk(self):
        name = input('이름은?')
        kor = int(input('국어는?'))
        eng = int(input('영어는?'))
        mat = int(input('수학은?'))

        return SungJukv8VO(name, kor, eng, mat)


    @staticmethod
    def load_sungjuk(self):

        global sjs  # 바깥에 생성(?) 된 sjs를 가져올 수 있음
        # 파일에 저장된 성적데이터를 모두 읽어 리스트에 저장
        try:
            with open('data/sungjuk8c.dat', encoding='UTF-8') as f:
                data = csv.reader(f)
                sjs = list(data)
        except:
            pass
    # 성적데이터들을 sungjuk8c.dat 파일에 저장
    # [ [혜교, 77, 33, 86]
    #   [지현, 77, 33, 86]
    #   [수지, 77, 33, 86]]

    @staticmethod
    def save_sungjuk(self, sjs):

        with open('data/sungjukv7c.dat', 'w', encoding='UTF-8', newline='') as f:
            # 방금 입력한 성적데이터와
            # 기존에 입력한 모든 성적 데이터를 csv 형식으로 파일에 함께 저장
            wf = csv.writer(f)     # csv 작업 초기화
            for sj in sjs :
                wf.writerow(sj)   # sjs 리스트의 요소를 csv 행으로 저장


    @staticmethod
    def add_sungjuk(self):
        # 성적 데이터 입력받기
        sj = self.input_sungjuk()

        # # 입력받은 성적데이터 초기화
        tot, avg, grd = compute_sungjuk(sj)

        # + : 2개의 리스트를 하나로 합쳐 하나의 리스트로 만듦
        sj = sj + [tot, avg, grd]

        sjs.append(sj)

        save_sungjuk(sjs)


    def read_sungjuk(self):
        hdr = '이름 국어 영어 수학\n'
        hdr += '------------------'
        print(hdr)

        for sj in sjs:
            print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]}')


    def read_one_sungjuk(self):
        name = input('조회할 학생의 이름은?')

        sj = None
        for item in sjs:
            if item['name'] == name: sj = item

        hdr = '이름 국어 영어 수학 총점 평균 학점\n'
        hdr = '------------------------------\n'
        print(hdr)
        print(f'{sj[0]} {sj[1]} {sj[2]} {sj[3]} {sj[4]} {sj[5]:.1f} {sj[6]}')


    def modify_sungjuk(self):
        name = input('수정할 데이터의 학생 이름은?')

        sj = None
        for i in range(len(sjs)):

            if sjs[i][0] == name:
                idx = i
                break

        # 새로운(기존) 값을 입력받음
        kor = int(input(f'새로운 국어는 ({sjs[idx][1]})?'))
        eng = int(input(f'새로운 영어는 ({sjs[idx][2]})?'))
        mat = int(input(f'새로운 수학는 ({sjs[idx][3]})?'))

        # 다시 성적 처리
        sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat}
        tot, avg, grd = computeSungJuk(sj)
        sj = sj + [tot, avg, grd]

        # 기존 위치에 다시 저장
        sjs[idx] = sj

        # 수정된 성적데이터를 파일에 저장
        save_sungjuk(sjs)

        # 삭제된 성적데이터를 파일에 반영
        sjs.pop(idx)

    def remove_sungjuk(self):
        name = input('삭제할 데이터의 학생 이름은?')

        idx = None
        for sj in sjs:  # 삭제할 데이터의 인덱스 조사
            if sj[0] == name:   # 만일 존재한다면
                sjs.remove(sj)  # 바로 데이터 삭제

                # 삭제된 성적데이터를 파일에 저장
                save_sungjuk(sjs)

    def compute_sungjuk(self, sj):
        tot = sj[1] + sj[2] + sj[3]
        avg = tot / 3
        grd = '가'
        if avg >= 90: grd = '수'
        elif avg >= 80: grd = '우'
        elif avg >= 70: grd = '미'
        elif avg >= 60: grd = '양'

        return tot, avg, grd













































