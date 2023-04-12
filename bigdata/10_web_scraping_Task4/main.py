# 문제4 : 할리스 전국 매장 정보 추출.
import requests
from bs4 import BeautifulSoup

no = 1
while(True):
    res = requests.get("https://www.hollys.co.kr/store/korea/korStore2.do?pageNo="+str(no))
    soup = BeautifulSoup(res.content, 'html.parser')

    for tr in soup.select_one('tbody').select('tr'):
        for td in len(tr.select('td')):
            print(tr.select('td')[td].text)
    no += 1