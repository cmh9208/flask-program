'''
과일 판매상에서 메뉴를 등록하는 어플을 제작하고자 합니다.
입력되는 값은 없다.
다만 실행했을 때 출력되는 결과는 다음과 같다.

3번 과일: 망고 가격: 5000원
********************************
'''
from util.common import Common

class Fruits(object):
    def __init__(self, number, name, pay):
        self.number = number
        self.name = name
        self.pay = pay

    def __str__(self):
        astar = "*"*40
        schema = "번호 이름 가격"
        return(f"{schema}\n{self.number}번 과일: {self.name} 가격: {self.pay}원\n{astar}")

    @staticmethod
    def del_fruits(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def print_fruitslist(ls):
        [print(i) for i in ls]

    @staticmethod
    def new_fruits():
        number = int(input("과일 번호: "))
        name = input("과일 이름: ")
        pay = int(input("과일 가격: "))
        return Fruits(number, name, pay)

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Common.print()
            if menu == 0:
                print("### 과일등록 ###")
                fruits = Fruits.new_fruits()
                ls.append(fruits)
            elif menu == 1:
                print("### 과일 목록 출력 ###")
                Fruits.print_fruitslist(ls)
            elif menu == 2:
                print("### 과일 삭제 ###")
                name = input("삭제할 과일: ")
                Fruits.del_fruits(ls, name)
            elif menu == 3:
                print("### 앱 종료 ###")
                break
            else:
                print("잘못된 번호 입니다.")

Fruits.main()


