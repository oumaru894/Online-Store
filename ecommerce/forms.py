from wtforms import  Form, StringField, TextAreaField, PasswordField, SubmitField, validators, EmailField, ValidationError
from flask_wtf.file import FileRequired, FileAllowed, FileField
from flask_wtf import FlaskForm
from flask import flash




class CustomerRegistrationForm(FlaskForm):
    name =  StringField('Name: ')
    username = StringField('username: ', [validators.DataRequired()])
    email = StringField('Email: ', [validators.Email(),validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired(), validators.EqualTo('confirm',message='Both password must match!')])
    confirm = PasswordField('Repeat password: ', [validators.DataRequired()])
    country = StringField('Country: ', [validators.DataRequired()])
    region = StringField('Region: ', [validators.DataRequired()])
    contact = StringField('Contact: ', [validators.DataRequired()])
    zipcode = StringField('Zip code: ', [validators.DataRequired()])
    address = StringField('Address: ', [validators.DataRequired()])
    
    profile = FileField('profile', validators=[FileAllowed(['jpg','png','gif','jpeg'], 'Image only please')])

    submit = SubmitField('Register')
    
    
    def validate_username(self, username):
        from model import Register
        if Register.query.filter_by(username=username.data).first():
            raise ValidationError("This email is already in use")

        
    def validate_email(self, email1):
        from model import Register
        if Register.query.filter_by(email=email1.data).first():
            raise ValidationError("This username is already in use")
        
            
class CustomerLoginFrom(FlaskForm):
    email = StringField('Email: ', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password: ', [validators.DataRequired()])


    