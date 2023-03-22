from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/direction')
def direction():
    return render_template("direction.html")


@app.route('/direction')
def about():
    return render_template("direction.html")


@app.route('/tour')
@app.route('/tour/')
def tour():
    return render_template("tour.html")


@app.route('/tour/russia')
def tour_russia():
    return render_template("russia.html")


@app.route('/tour/germany')
def tour_germany():
    return render_template("germany.html")


@app.route('/tour/apartment')
def tour_apartment():
    return render_template("apartment.html")


if __name__ == "__main__":
    app.run(debug=True)
