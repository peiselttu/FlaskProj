from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo,Length,ValidationError
from flaskblog.model import User

# construct the Registeration form
class RegisterationForm(FlaskForm):
    username=StringField("userName",validators=[DataRequired(),Length(2,10)])
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    confirm_password=PasswordField('ConfirmPassword',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Register')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("The username has already been taken. Please use another one.");


# Construct the Login Form
class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    # confirm_password=PasswordField('Confirm_Password',validators=[DataRequired(),EqualTo('passWord')])
    remember=BooleanField('Remember Me')
    submitLogin=SubmitField('Login')



