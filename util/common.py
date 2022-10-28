class Common(object):
    def __init__(self):
        pass

    @staticmethod
    def print(ls):
        for i, j in enumerate(ls):
            print(f"{i}번: {j}")
        return input("메뉴선택: ")
