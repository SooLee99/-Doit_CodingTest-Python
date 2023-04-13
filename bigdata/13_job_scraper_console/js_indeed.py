from bs4 import BeautifulSoup
from js_utils import get_selenium_web_driver


def find_indeed_jobs(keyword):
    results = []

    base_url = "https://kr.indeed.com/jobs?q="
    wd = get_selenium_web_driver()
    wd.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(wd.page_source, 'html.parser')
    wd.quit()

    jobs = soup.find_all(class_='resultContent')
    for job in jobs:
        link = ""
        title = ""
        company = ""
        location = ""

        job_title_tag = job.find('h2', class_='jobTitle')
        if job_title_tag:
            link = job_title_tag.a['href']
            title = job_title_tag.a.span.string

        company_location_tag = job.find('div', class_='company_location')
        if company_location_tag:
            company = company_location_tag.span.string
            location = company_location_tag.div.string

        job_post = {
            "link": f"https://kr.indeed.com{link}",
            "company": company.string,
            "title": title.string,
            "location": location.string
        }
        results.append(job_post)

    return results
