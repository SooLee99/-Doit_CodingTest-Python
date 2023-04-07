# blot.replit.com 페이지에서 블로그 제목과 날짜/저자 정보를 추출
import requests
from bs4 import BeautifulSoup

res = requests.get("https://blog.replit.com")
soup = BeautifulSoup(res.content, 'html.parser')
for tag in soup.find_all(class_='post-title'):
    print(tag.a.string.strip())
    print(tag.parent.h3.string.strip())
    print("----------------------------------")
    items = soup.select()

# article 태그
for article in soup.find_all('article', class_='post-item'):
    print(article.h1.a.string.strip())
    print(article.h3.string.strip())
    print("----------------------------------")

# 리스트 내에 for를 넣은 형태
article = [item for item in soup.find_all('article', class_='post-item')]
for i in range(len(article)):
    print(article[i].h1.a.string.strip())
    print(article[i].h3.string.strip())
    print('---------------------------------------')

# find로 나눈 형태
articles = soup.find_all("article")
for article in articles:
    title = article.find("h1").a.text.strip()
    date = article.find("h3").string.strip()
    print(f"{title}\n{date}")
    print('-------------------------------------------------------------')
