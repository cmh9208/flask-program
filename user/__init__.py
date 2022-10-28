from user.bmi import Bmi
from user.contact import Contact
from user.grade import Grade
from user.person import Person
from util.common import Common

ls = []
while True:
    menu = Common.print(["종료", "BMI", "주소록", "성적표", "개인정보"])
    if menu == 0:
        print("### 앱 종료 ###")
        break
    elif menu == 1:
        print("### BMI ###")
        submenu = Common.print(["종료", "BMI등록", "BMI목록", "BMI삭제"])
        if submenu == 0: break
        elif submenu == 1:
            biman = Bmi.new_bmi()
            ls.append(biman)
        elif submenu == 2:
            Bmi.print_bmi(ls)
        elif submenu == 3:
            name = input("삭제할 이름: ")
            Bmi.del_bmi(ls, name)
    elif menu == 2:
        print("### 주소록 ###")
        submenu = Common.print(["종료", "주소록등록", "주소록목록", "주소록삭제"])
        if submenu == 0:
            break
        elif submenu == 1:
            contact = Contact.new_contact()
            ls.append(contact)
        elif submenu == 2:
            Contact.print_contacts(ls)
        elif submenu == 3:
            name = input("삭제할 이름: ")
            Contact.delete_contacts(ls, name)
    elif menu == 3:
        print("### 성적표 ###")
        submenu = Common.print(["종료", "성적표등록", "성적표목록", "성적표삭제"])
        if submenu == 0:
            break
        elif submenu == 1:
            grade = Grade.new_grade()
            ls.append(grade)
        elif submenu == 2:
            Grade.print_grade(ls)
        elif submenu == 3:
            name = input("삭제할 이름: ")
            Grade.del_grade(ls, name)
    elif menu == 4:
        print("### 개인정보 ###")
        submenu = Common.print(["종료", "개인정보등록", "개인정보목록", "개인정보삭제"])
        if submenu == 0:
            break
        elif submenu == 1:
            person = Person.new_person()
            ls.append(person)
        elif submenu == 2:
            Person.print_person(ls)
        elif submenu == 3:
            name = input("삭제할 이름: ")
            Person.del_person(ls, name)
    else: print("잘못된 메뉴 번호 입니다.")