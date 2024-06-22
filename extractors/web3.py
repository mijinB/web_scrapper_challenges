import requests
from bs4 import BeautifulSoup, Tag


def extract_web3(keyword):
    response = requests.get(f"https://web3.career/{keyword}-jobs")
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("tbody", class_="tbody").find_all("tr")
    jobs_list = []

    for job in jobs:
        job_data = {
            "company": "",
            "position_title": "",
            "position_link": "",
            "skills": [],
        }

        company_parent = job.find("td", class_="job-location-mobile").children
        for el in company_parent:
            if type(el) == Tag:
                company_tag = el.find("h3")
                if company_tag is not None:
                    job_data["company"] = company_tag.text
        title_tag = job.find("h2", class_="my-primary")
        if title_tag is not None:
            job_data["position_title"] = title_tag.text
        link_tag = job.find("div", class_="job-title-mobile").children
        for el in link_tag:
            if type(el) == Tag:
                job_data["position_link"] = f"https://web3.career{el.attrs["href"]}"
        skill_parent = job.find_all("span", class_="my-badge-secondary")
        for parents in skill_parent:
            skill_tag = parents.children
            for el in skill_tag:
                if type(el) == Tag:
                    job_data["skills"].append(el.text)

        jobs_list.append(job_data)

    return jobs_list
