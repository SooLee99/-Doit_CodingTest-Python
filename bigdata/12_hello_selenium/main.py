from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
wd = webdriver.Chrome(options=options)
wd.get('https://kr.indeed.com/jobs?q=python')
# wd.execute_script('storePop2(333)')
time.sleep(1)

print(wd.page_source)
