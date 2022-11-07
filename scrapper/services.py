from urllib.request import urlopen

from bs4 import BeautifulSoup

from scrapper import MusicRanking


def BugsMusic(arg):
    arg = MusicRanking()
    soup = BeautifulSoup(urlopen(arg.url), 'lxml')
    title = {"class": arg.class_name[0]}
    artist = {"class": arg.class_name[1]}
    titles = soup.find_all(name=arg.class_name, attrs=title)
    artists = soup.find_all(name=arg.class_name, attrs=artist)

    # 디버깅 용
    [print(f"{k}. {i.find('a').text} : {j.find('a').text}")
     for i, j, k in zip(titles, artists, range(1, 100))]
    # dict 로 변화(데이터 프레임은 딕셔너리로 바꿔줘야함 키값이 있어서)
    for i in range(0, len(titles)):
        arg.dic[arg.titles[i]] = arg.artists[i] #타이틀을 키로 아티스트를 벨류로

    # csv 파일로 저장
    arg.dict_to_datafname()
    arg.dataframe_to_csv()