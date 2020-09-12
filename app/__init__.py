from flask import Flask
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)

# database assignment
import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite://:memory:', echo=True)
db =

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from app import routes, models
