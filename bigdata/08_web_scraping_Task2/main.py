# 문제2 : 가비아 컨테이너호스팅 페이지에서 Python 호스팅 정보 추출.

import requests
from bs4 import BeautifulSoup

res = requests.get("https://webhosting.gabia.com/container/service")
soup = BeautifulSoup(res.content, 'html.parser')

python_tab = soup.find(id="_tab1-2")
python_table = soup.find(class_="brick-plan-prod__table").find("tbody")

for tag in python_tab.find_all(class_='brick-plan-prod__name python'):
    print("종류 : " + tag.string)
    print(tag.find(class_='lib-mt-15').tbody)
