from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
wd = webdriver.Chrome(options=options)
wd.get('https://www.coffeebeankorea.com/store/store.asp')
wd.execute_script("storePop2(333)")
time.sleep(1)
soup = BeautifulSoup(wd.page_source, 'html.parser')

#matizCoverLayer0Content > div > div > div.store_txt

selector = '#matizCoverLayer0Content > div > div > div.store_txt'
store_txt = soup.select_one(selector)
print(store_txt.h2.string)

for store in store_txt.select('table tr'):
    print(f"{store.th.string}: {store.td.get_text()}")


