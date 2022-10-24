# 성적 데이터를 담고있는 저장하는 클래스와
# 성적 처리에 필요한 기능들로만 구성된 클래스로 나눠 작성

class SungJukVO:

    # 생성자
    def __init__(self, name, kor, eng, mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__avg = 0.0
        self.__grd = '가'

    def __str__(self):
        result = f'{self.__name} {self.__kor} {self.__eng} {self.__mat} ' \
                 f'{self.__tot} {self.__avg} {self.__grd}'
        return (result)

    # setter/getter
    # kor, eng, mat = getter
    # tot, avg = setter/getter
    # grd= setter

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kor(self):
        return self.__kor

    @kor.setter
    def kor(self, kor):
        self.__kor = kor

    @property
    def eng(self):
        return self.__eng

    @eng.setter
    def eng(self, eng):
        self.__eng = eng

    @property
    def mat(self):
        return self.__mat

    @mat.setter
    def mat(self, mat):
        self.__mat = mat

    @property
    def tot(self):
        return self.__tot

    @tot.setter
    def tot(self, tot):
        self.__tot = tot

    @property
    def avg(self):
        return self.__avg

    @avg.setter
    def avg(self, avg):
        self.__avg = avg

    @property
    def grd(self):
        return self.__grd

    @grd.setter
    def grd(self, grd):
        self.__grd = grd



class SungJukService:

    @staticmethod
    def read_sungjuk(self):
        name = input('이름은 ?')
        kor = int(input('국어는 ?'))
        eng = int(input('영어는 ?'))
        mat = int(input('수학은 ?'))

        return SungJukVO(name, kor, eng, mat)

    @staticmethod
    def compute_sungjuk(self, sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        if (sj.avg >= 90):sj.grd = '수'
        elif (sj.avg >= 80):sj.grd = '우'
        elif (sj.avg >= 70):sj.grd = '미'
        elif (sj.avg >= 60):sj.grd = '양'


sj = SungJukService.read_sungjuk()
SungJukService.compute_sungjuk(sj)

print(sj)


# setter 접근 제한하기 - inspect 모듈 이용
# sungjukservice 의 computesungjuk 함수에 의해서만
# tot, avg, grd 를 변경할 수 있도록 제한
sj.tot = 0 # computeSungJuk 함수 없이 개별적으로 변경 가능


