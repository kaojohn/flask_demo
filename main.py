from flask import Flask, render_template
from datetime import datetime
from pm25 import get_pm25

books = {1: "Python book", 2: "Java book", 3: "Flask book"}
app = Flask(__name__)


@app.route("/pm25")
def pm25_table():
    columns, values = get_pm25()
    return render_template("pm25.html", columns=columns, values=values)


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

    booktachi = {
        1: {
            "name": "Python book",
            "price": 299,
            "image_url": "https://im2.book.com.tw/image/getImage?i=https://www.books.com.tw/img/CN1/136/11/CN11361197.jpg&v=58096f9ck&w=348&h=348",
        },
        2: {
            "name": "Java book",
            "price": 399,
            "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/087/31/0010873110.jpg&v=5f7c475bk&w=348&h=348",
        },
        3: {
            "name": "C# book",
            "price": 499,
            "image_url": "https://im1.book.com.tw/image/getImage?i=https://www.books.com.tw/img/001/036/04/0010360466.jpg&v=62d695bak&w=348&h=348",
        },
    }

    # for id in booktachi:
    #     print(f'{id}:名稱:{booktachi[id]["name"]}價格:{booktachi[id]["price"]}')

    return render_template("books.html", books=booktachi)


@app.route("/")
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template("index.html", time=now, name="john")


app.run(debug=True)
