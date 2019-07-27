from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from models import User

class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(),Email()])
    password = PasswordField('Password',validators = [DataRequired()])
    submit = SubmitField("Login")

class RegistrationForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(),Email()])
    username = StringField('UserName',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(),EqualTo('pass_confirm',message = "Password Don't Match")])
    pass_confirm = PasswordField('Confirm Password',validators = [DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email = field.data).first():
            return True

    def check_username(self,field):
        if User.query.filter_by(username = field.data).first():
            return True
