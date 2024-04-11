'''import os
from app import route
from wtforms import  Form, StringField, TextAreaField, PasswordField, SubmitField, validators, EmailField, ValidationError

from flask_wtf import FlaskForm
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
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
#from model import Register




# Configure application
app = Flask(__name__)



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = Config.SECRET_KEY
Session(app)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///items.db")
app.config.from_object(Config)
dd = SQLAlchemy(app)'''

'''# Make sure API key is set
"""if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")"""


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response'''
