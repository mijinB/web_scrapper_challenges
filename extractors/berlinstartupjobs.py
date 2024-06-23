import requests
from bs4 import BeautifulSoup


def extract_berlin(keyword):
    response = requests.get(
        f"https://berlinstartupjobs.com/skill-areas/{keyword}/",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        },
    )
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find("ul", class_="jobs-list-items").find_all("li")
    jobs_list = []

    for job in jobs:
        job_data = {
            "company": "",
            "position_title": "",
            "position_link": "",
            "skills": [],
        }

        job_data["company"] = job.find("a", class_="bjs-jlid__b").text
        positions = job.find("h4", class_="bjs-jlid__h").children
        for position in positions:
            job_data["position_title"] = position.text
            job_data["position_link"] = position.attrs["href"]
        job_data["position_info"] = job.find("div", class_="bjs-jlid__description").text
        skills = job.find_all("a", class_="bjs-bl-whisper")
        for skill in skills:
            job_data["skills"].append(skill.text.replace("\n\t", ""))

        jobs_list.append(job_data)

    return jobs_list


extract_berlin("python")
