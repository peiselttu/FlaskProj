from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo,Length

# construct the Registeration form
class RegisterationForm(FlaskForm):
    username=StringField("userName",validators=[DataRequired(),Length(2,10)])
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('ConfirmPassword',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')


# Construct the Login Form
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('Confirm_Password',validators=[DataRequired(),EqualTo('passWord')])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')



