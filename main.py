from flask import Flask, render_template, request
from extractors.berlinstartupjobs import extract_berlin
from extractors.web3 import extract_web3
from extractors.weworkremotely import extract_wework

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    berlin = extract_berlin(keyword)
    web3 = extract_web3(keyword)
    wework = extract_wework(keyword)
    all_jobs = berlin + web3 + wework

    return render_template("search.html", keyword=keyword, jobs=all_jobs)


app.run("0.0.0.0")
