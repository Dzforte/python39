# 개선된 성적 클래스 - 생성자를 통해서 병수를 초기화

# self 무조건 써야함
class SungJukVO:
    def __init__(self, name, kor, eng, mat):
        self.__name = name
        self.__kor = kor
        self.__eng = eng
        self.__mat = mat
        self.__tot = 0
        self.__avg = 0.0
        self.__grd = ''

    # 출력전용 함수 (자바의 toString)
    # __str__ : 멤버변수들의 값을 문자열화해서
    # 객체 정보를 외부에 표현할 때 사용
    def __str__(self):
        self.computeSungJuk()
        result = f'{self.__name} {self.__kor} {self.__eng} {self.__mat} '\
                 f'{self.__tot} {self.__avg} {self.__grd}'
        return(result)

    def computeSungJuk(self):

        tot = self.__kor + self.__ng + self.__mat
        self.__avg = self.__tot / 3
        if (self.__avg >= 90):
            grd = '수'
        elif (self.__avg >= 80):
            grd = '우'
        elif (self.__avg >= 70):
            grd = '미'
        elif (self.__avg >= 60):
            grd = '양'

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


# 성적 객체 생성
sj = SungJukVO('혜교', 99, 98, 97)
print(sj)