import requests
import re

res = requests.get("http://goole.com")
print("응답코드 : ", res.status_code)
res.raise_for_status() # 문제 발생 시 종료

print(len(res.text)) # 웹 사이트에서 가져온 데이터 길이 확인

# 가져온 데이터를 파일로 만들어서 확인
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)



### 정규식 ###
# ex) cade
# . (ca.e) : 하나의 문자를 의미 -> care, cafe, case (O) / caffe(X)
# ^ (^de) : 문자열의 시작 -> desk, destination (O) / fade(X)
# $ (se$) : 문자열의 끝 -> case, base (O) / face(X)

# a = re.compile("정규식")
# b = a.match("비교할 문자열") : 문자열의 처음부터 순서대로 일치하는지 확인
# b = a.search("비교할 문자열") : 문자열 중 일치하는게 있는지 확인
# lst = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 반환

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

p = re.compile("ca.e")
m = p.match("case")
print_match(m)



# 유저 에이전트

