from flask import Flask, render_template, request, json
from utils.scraper import get_github_profile

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/profile", methods=["POST"])
def profile():
    if request.method == "POST":
        githubLink = request.form.get("githubLink")
        profile = get_github_profile(githubLink)
        return f'{profile}'