from ws_basic_util import get_soup
from ws_basic_util import print_store_info

# https://www.hollys.co.kr/store/korea/korStore2.do 페이지에서
# 전국매장 정보를 추출하여 화면에 출력
def scrape_hollys_stores_fixed_method(page_num):
    num_store = 0
    for i in range(page_num):
        # Get BeautifulSoup object
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i + 1}"
        soup = get_soup(url)
        if not soup:
            print(f"Error: invalid url - {url}")
            break

        # Scraping
        for tag in soup.find(class_='tb_store').tbody.find_all('tr'):
            num_store += 1
            print_store_info(tag)
            print("---------------------------------------" * 2)

        print(f"page[{i + 1}]=======================================" * 1)

    # Summary
    print(f"total # of stores: {num_store}")


# 고정된 page 개수를 사용하지 않는 방식1
def scrape_hollys_stores_dynimic_method1():
    num_store = 0
    page_index = 1
    while True:
        # Get BeautifulSoup object
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_index}"
        soup = get_soup(url)
        if not soup:
            print(f"Error: invalid url - {url}")
            break

        # Scraping
        tags = soup.find(class_='tb_store').tbody.find_all('tr')

        # Check if the curren page is valid
        if len(tags[0].find_all('td')) == 1:
            break

        for tag in tags:
            num_store += 1
            print_store_info(tag)
            print("---------------------------------------" * 2)

        print(f"page[{page_index}]=======================================" * 1)
        page_index += 1

    # Summary
    print(f"total # of stores: {num_store}")


# 고정된 page 개수를 사용하지 않는 방식2
def scrape_hollys_stores_dynimic_method2():
    num_store = 0
    page_index = 1
    while True:
        # Get BeautifulSoup object
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_index}"
        soup = get_soup(url)
        if not soup:
            print(f"Error: invalid url - {url}")
            break

        # Check if the curren page is valid
        if soup.find('td').string == '등록된 지점이 없습니다.':
            break

        # Scraping
        tags = soup.find(class_='tb_store').tbody.find_all('tr')

        for tag in tags:
            num_store += 1
            print_store_info(tag)
            print("---------------------------------------" * 2)

        print(f"page[{page_index}]=======================================" * 1)
        page_index += 1

    # Summary
    print(f"total # of stores: {num_store}")


# 고정된 page 개수를 사용하지 않는 방식3
def scrape_hollys_stores_dynimic_method3():
    num_store = 0
    page_index = 1
    while True:
        # Get BeautifulSoup object
        url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_index}"
        soup = get_soup(url)
        if not soup:
            print(f"Error: invalid url - {url}")
            break

        # Scraping
        tags = soup.find(class_='tb_store').tbody.find_all('tr')
        for tag in tags:
            num_store += 1
            print_store_info(tag)
            print("---------------------------------------" * 2)

        print(f"page[{page_index}]=======================================" * 1)

        # Check if the next page exists
        move_pages = soup.select('div.paging > a > img')
        if len(move_pages) == 0 or move_pages[-1].get('alt') != '다음10개':
            if soup.select('div.paging > a')[-1].string == str(page_index - 1):
                break

        page_index += 1

        # Summary
    print(f"total # of stores: {num_store}")
