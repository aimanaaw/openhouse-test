import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User, Session, Action

@app.route('/')
def hello():
    return "Hello World! Testing out the flask app"


@app.route('/<name>')
def user(name):
	return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()

