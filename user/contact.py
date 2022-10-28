'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
'''
from util.common import Common

class Contact(object):
    def __init__(self, name, phone_number, email, address) -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return (f"이름: {self.name} 전화번호: {self.phone_number} 이메일: {self.email} 주소: {self.address}")

    def print_info(self):
        print(self.name, self.phone_number, self.email, self.address)

    @staticmethod
    def delete_contacts(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def new_contact():
        name = input("이름: ")
        phone_number = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        return Contact(name, phone_number, email, address)

    @staticmethod
    def print_contacts(ls):
        [print(i) for i in ls]