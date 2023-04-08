# 문제1 : 가비아 라이브러리 페이지에서 게시판 제목/링크 추출.
"""
<div class="esg-content eg-post-12168 eg-grant-element-0-a">
    <a class="eg-grant-element-0 eg-post-12168" href="https://library.gabia.com/contents/12168/" target="_self">
        <span style="display: block;overflow: hidden; height: 25px; max-height: 25px">
            AWS 보안 가이드 ③ AWS 요금 폭탄을 피하는 법!
        </span>
    </a>
</div>
"""

import requests
from bs4 import BeautifulSoup

res = requests.get("https://library.gabia.com")
soup = BeautifulSoup(res.content, 'html.parser')

for title in soup.find_all('div', class_='eg-grant-element-0-a'):
    print(title.string)
    print(title.a['href'])
    print("----------------------------------")