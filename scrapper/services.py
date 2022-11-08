from bs4 import BeautifulSoup
from future.backports import urllib
import urllib.request as urllib
from urllib.request import urlopen

def BugsMusic(arg):
    # soup = BeautifulSoup(urlopen(arg.domain + arg.query_string), arg.parser)
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.Request(arg.domain + arg.query_string, headers=headers)
    a = urllib.urlopen(req)
    b = a.read().decode('utf-8')
    soup = BeautifulSoup(b, arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)

    # 디버깅 용
    [print(f"{i}위 {j.find('a').text} : {k.find('a').text}")
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    '''
    for i, j, k in zip(range(1, len(titles)), titles, artists):
        print(f"{i}위 {j.find('a').text} : {k.find('a').text}")
    '''
    # dict 로 변환(데이터 프레임은 키값이 있어 딕셔너리로 바꾸어야함)

    diction = {}
    print("#" * 10)
    print(len(titles))
    for i, j in zip(titles, artists):
        diction[j.find('a').text] = i.find('a').text
    print(diction)
    arg.diction = diction

    # csv 파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()


def MelonMusic(arg):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.Request(arg.domain + arg.query_string, headers=headers)
    a = urllib.urlopen(req)
    b = a.read().decode('utf-8')
    soup = BeautifulSoup(b, arg.parser)
    title = {"class": arg.class_names[0]}
    artist = {"class": arg.class_names[1]}
    titles = soup.find_all(name=arg.tag_name, attrs=title)
    artists = soup.find_all(name=arg.tag_name, attrs=artist)

    # 디버깅 용
    [print(f"{i}위 {j.find('a').text} : {k.find('a').text}")
     for i, j, k in zip(range(1, len(titles)), titles, artists)]
    '''
    for i, j, k in zip(range(1, len(titles)), titles, artists):
        print(f"{i}위 {j.find('a').text} : {k.find('a').text}")
    '''
    # dict 로 변환(데이터 프레임은 키값이 있어 딕셔너리로 바꾸어야함)

    diction = {}
    print("#" * 10)
    print(len(titles))
    for i, j in zip(titles, artists):
        diction[j.find('a').text] = i.find('a').text
    print(diction)
    arg.diction = diction

    # csv 파일로 저장
    arg.dict_to_dataframe()
    arg.dataframe_to_csv()

