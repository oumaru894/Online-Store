
import os
from wtforms import  Form, StringField, TextAreaField, PasswordField, SubmitField, validators, EmailField, ValidationError
from flask_wtf import FlaskForm
from cs50 import SQL
from flask import Flask,flash , redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup
from flask_msearch import Search
from config import Config
from helpers import lookup, usd
from datetime import datetime, timezone
from forms import CustomerRegistrationForm
from flask_restful import Api
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import secrets 
from pagination import page
# Configure application
app = Flask(__name__)
api = Api(app)

# Extend CSRF token lifetime (for testing, not recommended in production)
app.config['WTF_CSRF_TIME_LIMIT'] = 3600  # Set to a longer duration in seconds

# Configure session to use filesystem (instead of signed cookies) and setting secret key
app.config["SECRET_KEY"] = Config.SECRET_KEY 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI

Session(app)


# Configure CS50 Library to use SQLite database and sqlalchemy
db = SQL("sqlite:///items.db")
app.config.from_object(Config)
dd = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view="login"
login_manager.needs_refresh_message_category = "danger"
login_manager.login_message = u"please login first"


# Make sure API key is set
'''if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")'''

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    from model import Register
    if request.method == "GET":
    
        data = db.execute("SELECT * FROM items limit 8")
        return render_template("index.html", data=data)


#blog html
@app.route("/blog")
def blog():
    return render_template("blog.html")


#contact  html
@app.route("/contact")
def contact():
    return render_template("contact.html")


#about html
@app.route("/about")
def about():
    return render_template("about.html")


#registration of users in database
@app.route("/register", methods=["GET", "POST"])
def register():
    from model import Register
    # rendering registration template
    if request.method=="GET":
        return render_template("/register.html")
    
    else:
         #getting the user registration info
        username=request.form.get("username")
        password = request.form.get("password")
        confirmation=request.form.get("confirmation")
        person = request.form.get("person")
        number=request.form.get("number")
        
        #checking for errors
        if not username:
            return apology("require username")
        elif not password:
            return apology("require password")
        elif not confirmation:
            return apology("required confirmation")
        elif password != confirmation:
            return apology("passwords not match confirmation")
        elif password != confirmation:
            return apology("confirmation not match")
        else:
            duplicate = db.execute("SELECT username FROM users")
            for i in duplicate:
                if i["username"]==duplicate:
                    return apology("choose another username")
                
            hash=generate_password_hash(password)
            db.execute("INSERT INTO users (username, hash, name, contact) VALUES(?, ?, ?, ?)", username, hash, person, number)
            return redirect("/")
        return apology("Registeration Fialled")
 
@app.route('/result')
def result():
    from model import Register
    #selecting inout from search
    searchword = request.args.get("q")
    #quarying database for search items
    product = db.execute("select * from items where name like ? or description like ? limit 16", searchword, searchword)
    return render_template("result.html", product=product)

def MergeDict(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        final_dict = dict1 + dict2
        return final_dict
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        final_dict = dict(list(dict1.items()) + list(dict2.items()))
        return final_dict
    
@app.route("/carts", methods=["POST"])
def carts():
    from model import Register
    try:
        product_id = request.form.get("main_id")
        quantity = int(request.form.get("quantity"))
        product= db.execute("SELECT * FROM items WHERE id = ?", product_id)
        
        
        if product_id and quantity and request.method == "POST":
            DictItems = {product_id:{'name': product[0]["name"], 'path':product[0]["path"], 'price':product[0]["price"], 'quantity':quantity}}
            if "Carts" in session:
                print(session["Carts"])
                if product_id in session["Carts"]:
                    for key,i in session["Carts"].items():
                        if int(key) == int(product_id):
                            session.modified = True
                            i["quantity"] += 1
                else:
                    session["Carts"] = MergeDict(session["Carts"], DictItems)
            else: 
                session["Carts"] = DictItems
                return redirect(request.referrer)
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)
    
@app.route("/get_cart")
def get_cart():
    from model import Register
    if "Carts" not in session:
        return redirect('/store.html')
    total=0
    for key, i in session["Carts"].items():
        total += int(i['quantity']) * int(i['price'])
    return render_template("cart.html", total=total)


#delete from cart
@app.route("/delete_cart/<int:id>", methods=["POST","GET"])
def delete_cart(id):
    from model import Register
    if "Carts" in session and len(session["Carts"]) > 0:
        session.modified=True
        for key, i in session["Carts"].items():
            if int(key) ==id:
                session["Carts"].pop(key, None)
                if "Carts" in session and len(session["Carts"]) > 0:
                    return redirect(request.referrer)
        else:return redirect("/")
            
    else:
        return redirect("/")
        
@app.route("/clearcart")
def clearcart():
    from model import Register
    try:
        session.pop('Carts', None)
        return redirect("/store.html")
    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)    
            
            
@app.route("/update_cart",methods=["POST"])
def update_cart():
    from model import Register
    if request.method=="POST":
        id =  request.form.get("id")
        quantity = request.form.get("quantity")
        session.modified=True
        for key, i in session["Carts"].items():
            if int(key) == int(id):
                i["quantity"] = quantity
                flash(key)
        return redirect((request.referrer))
    
    return redirect((request.referrer))
@app.route("/emptyCart")
def emptyCart():
    from model import Register
    if len(session["Carts"]) > 0:
        session["Carts"].clear()
        return redirect("/")
    return redirect(request.referrer)
    
    

#check out function
@login_required
@app.route('/checkout')
def checkout():
    from model import Register
    if len(session["Carts"]) > 0:
        order = session["Carts"]
        return render_template("/checkout.html", order=order)
    return render_template("/store.html")
    


#store html
@app.route("/store.html")
def store():
    from model import Register
    if request.method == "GET":
        
        
        data = db.execute("SELECT * FROM items LIMIT 16")
        page1 = request.args.get('page')
        if page1 != None:
            page1=int(page1 )
            if page(page1, data):
                data = page(page1, data)
                return render_template("store.html", data=data)
        return render_template("store.html", data=data)
    

@app.route("/single_item.html/<int:id>")
def single_item(id):
    from model import Register
    main=db.execute("SELECT * FROM items WHERE id = ?",id)
    sub=db.execute("SELECT * FROM items WHERE name in (SELECT name items WHERE id =?) limit 3", id)
    data2 = db.execute("SELECT * FROM items LIMIT 8")
    return render_template("single_item.html",  main=main, sub=sub, data2=data2)

#CUSTOMER ACTIVITY CODING
@app.route('/c_register', methods=['GET','POST'])
def customer_register():
    from forms import CustomerRegistrationForm
    from model import Register
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        hash_password =generate_password_hash(form.password.data)
        register = Register(name=form.name.data, username=form.username.data, email=form.email.data,password=hash_password,country=form.country.data, region=form.region.data,contact=form.contact.data, address=form.address.data)
        dd.session.add(register)
        flash(f'Welcome {form.name.data} Thank you for registering', 'success')
        dd.session.commit()
        next = request.args.get('next')
        return redirect(next,url_for('login'))
    return render_template('c_register.html', form=form)


@app.route("/login", methods=["GET","post"])
def login():
    from forms import CustomerLoginFrom
    from model import Register
    form = CustomerLoginFrom()
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('you are login now', 'success')
            next = request.args.get('next')
            return redirect(next, url_for("store"))
        flash("your email or password is incorrect","danger")
        return redirect(request.referrer)
    redirect(url_for("store"))
    return render_template("/login.html", form=form)
        
@app.route("/logout")
def log_out():
    from model import Register
    logout_user()
    return redirect(url_for("login"))
    

#only get orders but does not display 
@app.route('/get_order')
@login_required
def get_order():
    from model import Register
    from model import CustomerOrder
    if current_user.is_authenticated:
        customer_id = current_user.id
        invoice = secrets.token_hex(5)
        try:    
            order = CustomerOrder(invoice=invoice, customer_id=customer_id,orders=session["Carts"])
            dd.session.add(order)
            dd.session.commit()
            flash("your order has been sent", "success")
            session.pop("Carts")
            return redirect(url_for('orders',invoice=invoice))
        except Exception as e:
        
            print(e)
            flash("something went wrong while getting order", "danger")
            return redirect(url_for('get_cart'))
        
#displaying customer orders
@app.route('/order/<invoice>')
@login_required
def orders(invoice):
    from model import Register
    from model import CustomerOrder

    if current_user.is_authenticated:
        grandtotal = 0
        subtotal = 0
        customer_id = current_user.id
        customer_name= Register.query.filter_by(name=current_user.name).first()
        customer = Register.query.filter_by(id=customer_id).first()
        order = CustomerOrder.query.filter_by(customer_id=customer_id).first()
        for key, product in order.orders.items():
            subtotal += float(product['price']) * int(product['quantity'])
    else:
        return redirect(url_for('login'))
    return render_template("order.html", invoice=invoice,subtotal=subtotal, customer_name=customer_name, customer=customer, order=order)


