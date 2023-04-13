# 1. replit.nix 수정 (hidden file)
~~~
  deps = [
    ...
    pkgs.chromium
    pkgs.chromedriver
  ];
~~~

# 2. selenium 패키지 설치

# 3. 예시
~~~
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
wd = webdriver.Chrome(options=options)
wd.get('https://www.google.com')
print(wd.page_source)
wd.quit()
~~~