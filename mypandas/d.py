def menu(ls):
    [print(f'{i}번{j}') for i,j in enumerate(ls)]
    return input('메뉴번호 선택: ')

list = ['111','222','333']

if __name__=="__main__":
    while True:
        menu = menu(list)
        if menu == '0':
            print('aaa')
        elif menu == '1':
            print('bbb')
        else:
            print('f')