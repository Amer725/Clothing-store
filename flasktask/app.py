from flask import Flask,render_template
app=Flask(__name__)


products=[
    {"id": 1, "name": "Classic White Tee", "price": "$20", "pic":"/static/taskpic/a.webp"},
    {"id": 2, "name": "Black Graphic Tee", "price": "$15" ,"pic":"/static/taskpic/b.webp"},
    {"id": 3, "name": "Blue Polo Shirt", "price": "$25" , "pic":"/static/taskpic/c.webp"},
    {"id": 4, "name": "Red V-neck Tee", "price": "$12" , "pic":"/static/taskpic/d.webp"},
    {"id": 5, "name": "Green Cotton Tee", "price": "$15" , "pic":"/static/taskpic/f.jpg"},]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/templates/index.html")
def indexhome():
    return render_template("index.html")

@app.route("/templates/menu.html")
def menu():
    return render_template("menu.html", products=products)


if __name__ == '__main__':
    app.run(debug=True)