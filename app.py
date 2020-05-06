from flask import Flask, render_template, redirect, url_for, flash

from forms import BookmarkForm

app = Flask(__name__)
app.config["SECRET_KEY"] = b'\x82\x8a\\\xb5\xbcd\x96\xb1\xb7das\x10e\x1b\x03'

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


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookmarkForm()

    if form.validate_on_submit():
        url = form.url.data
        continent = form.continent.data
        country = form.country.data
        city = form.city.data

        bm = {
            "user": "Magda",
            "url": url,
            "continent": continent,
            "country": country,
            "city": city
        }

        bookmarks.append(bm)
        flash(f"Stored {city}")
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
