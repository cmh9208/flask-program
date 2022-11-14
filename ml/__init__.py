from ml.stroke import STROKE_MENUS, stroke_menu
from ml.stroke import StrokeService

def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = StrokeService()
    while True:
        menu = my_menu(STROKE_MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("데이터구하기")
            t.spec()
        elif menu == '2':
            print("한글메타데이터")
            t.rename_meta()
        elif menu == '3':
            print("타깃변수설정")
            t.target()
        elif menu == '4':
            print("데이터처리")
            t.data_processing()
        elif menu == '5':
            print("시각화")
        elif menu == '6':
            print("모델링")
        elif menu == '7':
            print("학습")
        elif menu == '8':
            print("예측")
        else:
            try:
                stroke_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")
