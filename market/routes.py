from market import app
from market.db_models import Item
from flask import render_template


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")
    
@app.route("/market")
def market_page():
    items = Item.query.all()
    # items = [
    #     {"id": 1, "name": "Phone", "barcode": "123412341234", "price": 500},
    #     {"id": 2, "name": "Laptop", "barcode": "123412341235", "price": 900},
    #     {"id": 3, "name": "Keyboard", "barcode": "123412341236", "price": 150}
    # ]
    return render_template("market.html", items=items)
    
@app.route("/about")
def about_page():
    return render_template("about.html")
    
    