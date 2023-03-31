# blot.replit.com 페이지에서 블로그 제목과 날짜/저자 정보를 추출
import requests
from bs4 import BeautifulSoup

res = requests.get("https://blog.replit.com")
soup = BeautifulSoup(res.content, 'html.parser')
for tag in soup.find_all(class_='post-title'):
    print(tag.a.string.strip())
    print(tag.parent.h3.string.strip())
    print("----------------------------------")