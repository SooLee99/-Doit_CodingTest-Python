import requests
from bs4 import BeautifulSoup


def find_wework_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    res = requests.get(f"{base_url}{keyword}")
    if res.status_code != 200:
        print(f"Http Response Error: {res.status_code}")
        return

    results = []
    soup = BeautifulSoup(res.content, 'html.parser')
    job_sections = soup.find_all('section', class_='jobs')
    for job_section in job_sections:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for job in job_posts:
            link = job.a['href']
            company, _, location = job.find_all(class_='company')
            title = job.find(class_='title')
            job_post = {
                "link": f"https://weworkremotely.com{link}",
                "company": company.string,
                "title": title.string,
                "location": location.string
            }
            results.append(job_post)

    return results
