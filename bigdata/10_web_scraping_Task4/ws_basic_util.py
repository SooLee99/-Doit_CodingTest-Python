import time
import requests
from bs4 import BeautifulSoup

def get_soup(url, encoding=None):
    try:
        res = requests.get(url)
        time.sleep(1)
        return BeautifulSoup(res.content, 'html.parser', from_encoding=encoding)
    except:
        return None

def print_store_info(store_tag):
    tds = store_tag.find_all('td')
    print(tds)
    # 지역	매장명	현황	주소	매장서비스	전화번호
    region = tds[0].string
    name   = tds[1].a.string
    status = tds[2].string
    addr   = tds[3].a.string
    services = []
    for img_tag in tds[4].find_all('img'):
        services.append(img_tag.get('alt', "").strip())
    phone  = tds[5].string
    print(region, name, status, addr, "/".join(services), phone, sep='|')
