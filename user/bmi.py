'''
이름, 키, 몸무게를 입력받아서 비만도를 측정하고
입력, 출력, 삭제하는 프로 그램을 만드시오.

bmi 지수를 구하는 공식은 다음과 같다
bmi지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))

고도 비만 : 35 이상
중도 비만 (2단계 비만) : 30 -34.9
경도 비만 (1단계 비만) : 25 -29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
'''

class Bmi(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg

    def set_bmi(self):
        m = self.cm/100
        bmi = self.kg/(m*m)
        return bmi

    def get_bmi(self):
        bmi = self.set_bmi()
        if bmi >= 35:
            biman = "고도 비만"
        elif bmi >= 30:
            biman = "중도 비만"
        elif bmi >= 25:
            biman = "경도 비만"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        return biman

    def __str__(self):
        astar = "*"*50
        return (f"이름: {self.name} 키: {self.cm} 몸무게: {self.kg} bmi: {self.get_bmi()}\n{astar}")

    @staticmethod
    def del_bmi(ls, name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def print_bmi(ls):
        [print(i) for i in ls]

    @staticmethod
    def new_bmi():
        name = input("이름: ")
        cm = float(input("키: "))
        kg = float(input("몸무게: "))
        return Bmi(name, cm, kg)