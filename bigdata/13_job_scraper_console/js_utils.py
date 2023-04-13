from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_selenium_web_driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

"""
job = {
    'title': 'value',
    'link': 'value',
    'company': value,
    'location' : value
}
"""
def print_jobs(jobs):
    for i, job in enumerate(jobs):
        print(f"[{i+1}] {job['title']}")
        print(job['link'])
        print(f"{job['company']}, {job['location']}")
        print("-------------------------------------------------")