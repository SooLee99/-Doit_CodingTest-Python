# 문제4 : 할리스 전국 매장 정보 추출.
import requests
from bs4 import BeautifulSoup

i = 0
out = True

while(out):
    i+=1
    res = requests.get("https://www.hollys.co.kr/store/korea/korStore2.do?pageNo="+str(i))
    soup = BeautifulSoup(res.content, 'html.parser')
    tbody = soup.select_one('tbody')

    for store_tr in tbody.select('tr'):
        if(store_tr.td.string=='등록된 지점이 없습니다.'):
            out=False
            break

        for store_td in store_tr.select('td'):
            print(store_td.string,end='|')
        print('\n------------------------------')
