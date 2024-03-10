from flask import Flask, render_template, request, jsonify
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
        return render_template('profile.html', profile_image = profile["profile_image"], profile_name = profile["profile_name"])