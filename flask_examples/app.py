from flask import Flask, render_template, request

from models import books
from services import MathService

app = Flask(__name__)


# GET /  -> http://localhost:5000

@app.route("/")
def hello():
    return render_template(
        "home.html",
        tresc="Hello Stranger!!",
        lista=[1, 2, 3],
        xxx="od czapy",
        flaga=False,

    )


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}!!"


@app.route("/maths/<op>/<int:a>/<int:b>")
def maths(op, a, b):
    result = MathService().handle(op, a, b)
    return render_template(
        "maths.html",
        result=result
    )


@app.route("/books/")  # /books/     /books/?query=Pan
def books_list():

    q = request.args.get("query")
    books_list = books
    if q:
        books_list = [x for x in books_list if x.title.startswith(q)]

    return render_template(
        "list.html",
        objects=books_list

    )


"/maths/add/1/3/"
"/maths/sub/1/3/"

"/books/?q=Pan"

# ustawienie zmiennej środowiskowej (environment variable)
# set FLASK_ENV=development # windows
# export FLASK_ENV=development
