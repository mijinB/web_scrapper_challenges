import requests
from bs4 import BeautifulSoup


def extract_wework(keyword):
    response = requests.get(
        f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    )
    soup = BeautifulSoup(response.text, "html.parser")
    sections = soup.find_all("section", class_="jobs")
    li_all = []
    jobs = []
    jobs_list = []

    for section in sections:
        li_list = section.find_all("li")
        for el in li_list:
            li_all.append(el)
    for li in li_all:
        if li.get("class") != ["view-all"]:
            jobs.append(li)

    for job in jobs:
        job_data = {
            "company": "",
            "position_title": "",
            "position_link": "",
            "location": "",
        }

        job_data["company"] = job.find("span", class_="company").text
        job_data["position_title"] = job.find("span", class_="title").text
        link_text = job.find("a", recursive=False).attrs["href"]
        job_data["position_link"] = f"https://weworkremotely.com{link_text}"
        job_data["location"] = job.find("span", class_="region").text

        jobs_list.append(job_data)

    return jobs_list
