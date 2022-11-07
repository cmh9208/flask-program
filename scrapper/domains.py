import urllib
from dataclasses import dataclass
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from const.path import CTX

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""
'''
class BugsMusic(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        _ = 0
        title = {"class":"title"}
        artist = {"class":"artist"}
        titles = soup.find_all(name="p", attrs=title)
        artists = soup.find_all(name="p", attrs=artist)

        [print(f"{k}. {i.find('a').text} : {j.find('a').text}")
         for i,j,k in zip(titles, artists, range(1, 100))]

class Melon(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers= self.headers)
        title = {"class":"ellipsis rank01"}
        artist = {"class":"ellipsis rank02"}
        titles = req.find_all(name="a", attrs=title)
        artists = req.find_all(name="a", attrs=artist)
        [print(f"{k}. {i.find('a').text} : {j.find('a').text}")
         for i, j, k in zip(titles, artists, range(1, 100))]
'''


'''
for i in titles:
    print(f"{i.find('a').text}")
print("*********")
for i in artists:
    print(f"{i.find('a').text}")
'''
@dataclass
class MusicRanking:
    html : str
    soup : BeautifulSoup
    parser: str
    domain : str
    query_string : str
    headers : dict
    tag_name : str
    fname : str
    class_name : list
    artists : list
    titles : list
    dic : dict
    df : None


    @property
    def html(self) -> str: return self.html

    @html.setter
    def html(self, html): self.html = html

    @property
    def soup(self) -> BeautifulSoup: return self.soup

    @soup.setter
    def soup(self, soup): self.soup = soup

    @property
    def parser(self) -> str: return self.parser

    @parser.setter
    def parser(self, parser): self.parser = parser

    @property
    def domain(self) -> str: return self.domain

    @domain.setter
    def domain(self, domain): self.domain = domain

    @property
    def query_string(self) -> str: return self.query_string

    @query_string.setter
    def query_string(self, query_string): self.query_string = query_string

    @property
    def headers(self) -> dict: return self.headers

    @headers.setter
    def headers(self, headers): self.headers = headers

    @property
    def tag_name(self) -> str: return self.tag_name

    @tag_name.setter
    def tag_name(self, tag_name): self.tag_name = tag_name

    @property
    def fname(self) -> str: return self.fname

    @fname.setter
    def fname(self, fname): self.fname = fname

    @property
    def class_names(self) -> list: return self.class_names

    @class_names.setter
    def class_names(self, class_names): self.class_names = class_names

    @property
    def artists(self) -> list: return self.artists

    @artists.setter
    def artists(self, artists): self.artists = artists

    @property
    def titles(self) -> list: return self.titles

    @titles.setter
    def titles(self, titles): self.titles = titles

    @property
    def dic(self) -> dict: return self.dic

    @dic.setter
    def dic(self, dic): self.dic = dic

    @property
    def df(self) -> None: return self.df

    @df.setter
    def df(self, df): self.df = df

    ### DB에 저장하는 코드 ###

    # 딕셔너리를 데이터 프레임으로 저장
    def dict_to_datafname(self):
        self.df = pd.DataFrame.from_dict(self.dic, orient="index")

     # 데이터 프레임을 csv로
    def dict_to_datafname_to_csv(self):
        path = CTX+ self.fname+'.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN")



