import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "thisissupposedtobeasecret"
basedir = os.path.abspath(os.path.dirname(__file__))
#  *** THIS IS A CONNECTION SCHEME SYNTAX WHEN CONNECTING TO A POSTGRESSQL DATABASE ***

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"



app.config['SQLALCHEMY_DATABASE_URI']="postgresql://postgres:postgres@localhost:5432/blogpediadb"
app.config['SQLALCHEMY_TRACK_MODIFICATION']= False

db = SQLAlchemy(app)

migrate = Migrate(db, app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
