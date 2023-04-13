from js_wework import find_wework_jobs
from js_indeed import find_indeed_jobs
from js_utils import print_jobs

keyword = input('Enter Keyword: ')
if keyword:
    results = []

    temp = find_wework_jobs(keyword)
    if temp:
        results += temp

    temp = find_indeed_jobs(keyword)
    if temp:
        results += temp

    print("")
    print_jobs(results)