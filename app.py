from flask import Flask, render_template

app = Flask(__name__)

user = "David"


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", user=user)


@app.route("/add")
def add():
    return render_template("add.html")


if __name__ == "__main__":
    app.run()
