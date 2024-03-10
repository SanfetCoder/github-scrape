from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/profile", methods=["POST"])
def profile():
    if request.method == "POST":
        githubLink = request.form.get("githubLink")
        return f'{githubLink}'