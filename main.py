from flask import Flask, render_template, request
from extractors.berlinstartupjobs import extract_berlin

app = Flask("JobScrapper")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    jobs = extract_berlin(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
