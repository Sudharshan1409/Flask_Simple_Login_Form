import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = 'User'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64),unique = True,index = True)
    username = db.Column(db.String(64),unique = True,index = True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
