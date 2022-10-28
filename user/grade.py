'''
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
홍길동 90 90 92 272 90.6 A
홍길동 90 90 92 272 90.6 A
********************************
'''
from util.common import Common

class Grade(object):
    def __init__(self, name, ko, en, ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma

    def set_total(self):
        total = self.ko + self.en + self.ma
        return total

    def set_avg(self):
        avg = self.set_total()/3
        return avg

    def get_grade(self):
        avg = self.set_avg()
        if avg >=90: grade = "A"
        elif avg >= 80: grade = "B"
        elif avg >= 70: grade = "C"
        elif avg >= 60: grade = "D"
        elif avg >= 50: grade = "E"
        else: grade = "F"
        return grade

    def __str__(self):
        astar = "*"*50
        schema = "국어, 영어, 수학, 총점, 평균, 학점"
        return(f"{schema}\n{self.ko} {self.en} {self.ma} {self.set_total()} {self.set_avg()} {self.get_grade()}\n{astar}")

    @staticmethod
    def del_grade(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def print_grade(ls):
        [print(i) for i in ls]

    @staticmethod
    def new_grade():
        name = input("이름: ")
        ko = int(input("국어 점수: "))
        en = int(input("영어 점수: "))
        ma = int(input("수학 점수: "))
        return Grade(name, ko, en, ma)

