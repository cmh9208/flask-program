from scrapper.domains import MusicRanking
from scrapper.view import ScrapController

if __name__=="__main__":
    m = MusicRanking()
    while True:
        menu = input("0번:종료,1번:벅스,2번:멜론")
        api = ScrapController()
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print("벅스")
            m.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_string = "20221101"
            m.parser = "lxml" # lxml은 구문을 분석하기 위한 파서
            m.class_names=["title", "artist"]
            m.tag_name = "p"
            api.menu_1(m) # 도메인을 던져줌

        elif menu == "2":
            print("멜론")
            m.domain = "https://www.melon.com/chart/index.htm?dayTime="
            m.query_string ="2022110810"
            m.parser = "lxml"
            m.class_names = ["ellipsis rank01","ellipsis rank02"]
            m.tag_name = "div"
            api.menu_2(m)
        else:
            print("해당메뉴 없음")