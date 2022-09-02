from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField
from wtforms.validators import Email, EqualTo, ValidationError, DataRequired
from models import User

# Registration Form
class RegisterForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('Email')
    password = PasswordField('Password', validators=[EqualTo('confirm_password', 
                                                             message="Passwords must match")])
    confirm_password = PasswordField('Confirm Password')
    terms = BooleanField('Terms')
    
    # Prevent duplicate username
    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            raise ValidationError("Username already exists. Choose a different one")
        
    # Prevent duplicate email
    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError("Email already exists. Choose a different one")

# Login Form
class LoginForm(FlaskForm):
    username = StringField('Username')
    password = StringField('Password')
    remember_me = BooleanField('Remember Me')
    
# Recover Password Form
class RecoverPasswordForm(FlaskForm):
    email = EmailField('Email')
    
# Password Reset Form
class ResetPasswordForm(FlaskForm):
    password = PasswordField('New Password')
    confirm_password = PasswordField('Confirm Pasword', 
                                     validators=[EqualTo('password', message="Passwords must match")])