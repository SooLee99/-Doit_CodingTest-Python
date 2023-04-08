# 문제3 : 네이버 증권 페이지에서 코스피 종목 정보 추출.
import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/sise/sise_quant.naver")
soup = BeautifulSoup(res.content.decode('euc-kr','replace'), 'html.parser')

for title in soup.find_all('a',class_='tltle'):
    print(title.string)