import requests
from bs4 import BeautifulSoup

def crawling(soup):
    # soup 객체에서 추출해야 하는 정보를 찾고 반환
    # 이전 글 영화 리뷰 추출 방식과 동일
    result = []
    ul = soup.find("ul", class_="rvw_list_area")

    for li in ul.find_all("li"):
        result.append(li.find("strong").get_text())

    return result


def get_href(soup):
    # 검색 결과, 가장 위에 있는 영화로 접근할 수 있는 href를 반환
    a = soup.find("ul", class_="search_list_1").find("a")

    href = a['href'].replace('basic', 'review')

    return "https://movie.naver.com" + href


def get_url(movie):
    # 입력된 영화를 검색한 결과의 url을 반환
    # 문자열 중간에 변수를 넣기 위해서는 앞따옴표 앞에 f라고 적고 대괄호 안에 변수를 넣어주면 됨
    return f"https://movie.naver.com/movie/search/result.nhn?query={movie}&section=all&ie=utf8"


def main():
    list_href = []

    custom_header = {
        'referer': 'https://www.naver.com/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }

    # 섹션을 입력
    movie = input('영화 제목을 입력하세요. \n  > ')

    url = get_url(movie)
    print(url)
    req = requests.get(url, headers=custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    movie_url = get_href(soup)
    print(movie_url)

    href_req = requests.get(movie_url)
    href_soup = BeautifulSoup(href_req.text, "html.parser")

    list_href = crawling(href_soup)
    print(list_href)


if __name__ == "__main__":
    main()