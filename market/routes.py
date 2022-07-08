from market import app
from market.db_models import Item
from flask import render_template
from market.forms import RegisterForm


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")
    
@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)
    
@app.route("/about")
def about_page():
    return render_template("about.html")
    
@app.route("/register")
def register_page():
    form = RegisterForm()
    return render_template("register.html", form=form)