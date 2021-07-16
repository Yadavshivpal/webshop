from flask import Flask, redirect, request, jsonify, Response,render_template,url_for
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["inventory"]
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/add", methods=['POST'])
def add():
    item_description = request.form.get("name")
    item_price = request.form.get("price")
    mydict = { "name": item_description, "price": item_price }
    x = mycol.insert_one(mydict)
    return render_template('add.html')

@app.route("/update")
def update():
    item_description = request.values.get("name")
    mycol.delete_one( { "name": item_description } )
    return render_template('update.html')


@app.route("/print")
def print():
    li = mycol.find()
    return render_template('print.html',list=li)

@app.route("/buy")
def buy():
    item_price = 0
    item_description = request.values.get("name")
    x = mycol.find({"name": item_description})
    return render_template('buy.html',records=x)

if __name__ == "__main__":
    app.run(debug=True)
