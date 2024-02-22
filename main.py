from flask import Flask
from datetime import datetime

books = {1: "Python book", 2: "Java book", 3: "Flask book"}
app = Flask(__name__)


@app.route("/sum/x=<a>&y=<b>")
def get_sum(a, b):
    try:
        return f"{a}+{b}的總合為:{eval(a)+eval(b)}"
    except Exception as e:
        print(e)
        return "輸入錯誤"


@app.route("/books/<int:id>")
def get_book(id):
    try:
        return books[id]
    except Exception as e:
        print(e)
        return "書籍編號錯誤"


@app.route("/books")
def get_books():
    return books


@app.route("/")
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>{now}</h1>"


app.run(debug=True)
