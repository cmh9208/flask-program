from scrapper.domains import MusicRanking
from scrapper.view import ScrapController

if __name__ == "__main__":
    m = MusicRanking()
    api = ScrapController()
    while True:
        menu = input("0번 종료, 1번 벅스")
        if menu == "0":
            print("종료")
            break

        elif menu == "1":
            print("벅스")
            m.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_string = "20221106"
            m.parser = "lxml"
            m.class_names.append("title", "artist")
            m.tag_name = "p"
            api.menu_1(m) # 도메인을 던져줌

        else:
            print("해당메뉴 없음")
