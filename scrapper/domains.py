from dataclasses import dataclass
import pandas as pd
from bs4 import BeautifulSoup
from const.path import CTX

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.

class BugsMusic:
    def __init__(self, url):
        self.url = url
    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        title={"class":"title"}
        artist = {"class":"artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)
        [print(f"{i}위 {j.find('a').text} : {k.find('a').text}")
         for i, j, k in zip(range(1,len(titles)), titles, artists)]
class Melon:
    pass
"""
@dataclass
class MusicRanking:
    html = ''
    parser = ''
    domain = ''
    query_string = ''
    headers = {}
    tag_name = ''
    fname = ''
    class_names = []
    artists = []
    titles = []
    diction = {}
    df = None

# parser : srt  (선언)
# 디크레이션

# parser = ''   (할당)
# 어사이먼트(위도,경도 존재)(메모리 용량 차지)

    def dict_to_dataframe(self):
        print(len(self.diction))
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')
        # orient='index' 왼쪽 아래로 인덱스를 줘라

    def dataframe_to_csv(self):
        path = './save/result.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header=None)