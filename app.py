import os
from flask import Flask, abort, render_template, redirect, request, jsonify, flash, url_for
from flask_sqlalchemy import SQLAlchemy
# from upload-form import NewLog
from sqlalchemy.dialects.postgresql import JSON
from forms import NewLog, SearchForm
# from models.model import User, Session, Action

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.model import User, Session, Action



@app.route('/')
@app.route('/home')
def home():
	temp = db.select([Session])
	payload = db.session.query(User, Session, Action).select_from(User).join(Session).join(Action).all()

	print(payload)
	entries = Action.query.all()
	
	dump = []
	for each in entries:
		# print(each.time)
		dump.append({each.session_id: {
			"type": each.type,
			"time": each.time,
			"properties": each.properties
			}})
	# print('dump', dump)
	return jsonify(dump), 201



@app.route('/upload', methods=['GET', 'POST'])
def upload():
	user = User(id = 'AAA500')
	db.session.add(user)
	db.session.commit()
	session = Session(id = 'BBB900', user_id = 'AAA500')
	db.session.add(session)
	db.session.commit()
	action = Action(time = "2018-10-18T21:37:28-06:00", type = "CLICK", properties = {
		"locationX": 52,
		"locationY": 11
	  }, session_id = 'BBB900')
	db.session.add(action)
	db.session.commit()
	resultArray = action

	return action, 201


@app.route('/search', methods=['GET', 'POST'])
def queryData():
	form = SearchForm()
	dump = []
	payload = db.session.query(User, Session, Action).select_from(User).join(Session).join(Action).all()
	print('testing', payload)
	for eachItem in payload:
		dump.append({
			eachItem[0].id: {
			"sessionId": eachItem[1].id,
			"actions": {
			"type": eachItem[2].type,
			"time": eachItem[2].time,
			"properties": eachItem[2].properties
			}
			}
			})
	return jsonify(dump), 201

if __name__ == '__main__':
	app.run()

