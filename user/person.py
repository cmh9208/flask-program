'''
이름, 주민번호(950101-1), 주소를 입력박아서
회원명부를 관리하는 어플을 제작하고자 한다.

출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25세 (만나이)
성별: 남성
주소: 서울
********************************
'''

class Person(object):
    def __init__(self, name, num, juso):
        self.name = name
        self.num = num
        self.juso = juso

    def set_aeg(self):
        a = int(self.num[0:2])
        b = a + 1900
        c = 2022 - b
        return c

    def set_gendr(self):
        d = int(self.num[8])

        if d == 1:
            e = "남성"
        elif d == 2:
            e = "여성"
        elif d == 3:
            e = "남성"
        elif d == 4:
            e = "남성"
        else:
            e = "잘못된 주민번호 입니다."
        return e

    def __str__(self):
        name = self.name
        juso = self.juso
        astar = "*" * 40
        return (f"이름: {name}\n나이: {self.set_aeg()}\n성별: {self.set_gendr()}\n주소: {juso}\n{astar}")

    @staticmethod
    def print_person(ls):
        [print(i) for i in ls]

    @staticmethod
    def del_person(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def new_person():
        name = input("이름: ")
        num = input("주민번호: ")
        juso = input("주소: ")
        return Person(name, num, juso)