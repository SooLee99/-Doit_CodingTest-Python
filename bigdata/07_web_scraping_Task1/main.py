# 문제1 : 가비아 라이브러리 페이지에서 게시판 제목/링크 추출.
import requests
from bs4 import BeautifulSoup

res = requests.get("https://library.gabia.com")
soup = BeautifulSoup(res.content, 'html.parser')

for title in soup.find_all('div', class_='eg-grant-element-0-a'):
    print(title.string)
    print(title.a['href'])
    print("----------------------------------")