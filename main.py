from flask import Flask, render_template, request
from extractors.berlinstartupjobs import extract_berlin

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def hello():
    all_jobs = {}
    keyword = request.args.get("keyword")
    all_jobs["berlin"] = extract_berlin(keyword)
    print(all_jobs)

    return render_template("search.html", keyword=keyword, jobs=all_jobs)


app.run("0.0.0.0")
