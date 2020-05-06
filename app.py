from flask import Flask, render_template

app = Flask(__name__)

bookmarks = [
    {
        "user": "Tom",
        "url": "https://en.wikivoyage.org/wiki/Karlsruhe",
        "continent": "Europe",
        "country": "Deutschland",
        "city": "Karlsruhe"
    },
    {
        "user": "Katie",
        "url": "https://en.wikivoyage.org/wiki/Split",
        "continent": "Europe",
        "country": "Croatia",
        "city": "Split"
    },
    {
        "user": "Anna",
        "url": "https://en.wikivoyage.org/wiki/Vienna",
        "continent": "Europe",
        "country": "Austria",
        "city": "Vienna"
    }
]

def get_latest_place(limit):
    return bookmarks[:limit]

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", bookmarks=get_latest_place(5))


@app.route("/add")
def add():
    return render_template("add.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
