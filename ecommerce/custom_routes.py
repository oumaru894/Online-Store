import os
from app import app
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

'''@app.route("/custom_registration", method=['POST','GET'])
def customer_register():
    form = CustomerRegistrationForm(request.form)
    return render_template('/custom_registration.html', form)'''