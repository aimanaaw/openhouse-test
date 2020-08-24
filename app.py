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



# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.String, primary_key=True, nullable=False)

#     def __init__(self, id):
#         self.id = id

#     def __repr__(self):
#         return '<id {}>'.format(self.id)


# class Session(db.Model):
#     __tablename__ = 'sessions'

#     id = db.Column(db.String, primary_key=True)
#     user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

#     def __init__(self, id, user_id):
#         self.id = id
#         self.user_id = user_id


#     def __repr__(self):
#         return '<id {}>'.format(self.id)


# class Action(db.Model):
#     __tablename__ = 'actions'

#     id = db.Column(db.Integer, primary_key=True)
#     time = db.Column(db.DateTime)
#     type = db.Column(db.Text)
#     properties = db.Column(JSON)
#     session_id = db.Column(db.String, db.ForeignKey('sessions.id'))

#     def __init__(self,time, type, properties, session_id):
#         # self.id = id
#         self.time = time
#         self.type = type
#         self.properties = properties
#         self.session_id = session_id

#     def __repr__(self):
#         return '<id {}>'.format(self.id)


@app.route('/')
@app.route('/home')
def home():
	temp = db.select([Session])
	print(temp)
	# entries = db.select([User, Session, Action])
	entries = Action.query.all()
	
	dump = []
	for each in entries:
		print(each.time)
		dump.append({each.session_id: {
			"type": each.type,
			"time": each.time,
			"properties": each.properties
			}})
	print('dump', dump)
	return render_template('home.html', actionLogs = dump)


# @app.route('/')
# @app.route('/home')
# def home():
# 	temp = db.select([Session])
# 	print(temp)
# 	# entries = db.select([User, Session, Action])
# 	entries = Action.query.all()
	
# 	dump = []
# 	for each in entries:
# 		dump.append({each.session_id: {
# 			"type": each.type,
# 			"time": each.time,
# 			"properties": each.properties
# 			}})
# 	return jsonify(dump)



@app.route('/upload', methods=['GET', 'POST'])
def upload():
	# user = User(id = 'MMM155')
	# db.session.add(user)
	# db.session.commit()
	# session = Session(id = 'JJL139', user_id = 'MMM155')
	# db.session.add(session)
	# db.session.commit()
	# action = Action(time = "2018-10-18T21:37:28-06:00", type = "CLICK", properties = {
	# 	"locationX": 52,
	# 	"locationY": 11
	#   }, session_id = 'JJL139')
	# db.session.add(action)
	# db.session.commit()
	# print(user)
	# print(session)
	# resultArray = action
	form = NewLog()
	if form.validate_on_submit():
		flash(f'Log submitted for {form.user_id.data}', 'successful')
		return redirect(url_for('home'))
	return render_template('data-form.html', title='Upload', form = form)

	# return 'done', 201



@app.route('/search', methods=['GET', 'POST'])
def queryData():
	form = SearchForm()
	if form.validate_on_submit():
		flash(f'Log submitted for {form.user_id.data}', 'successful')
		return 'query data', 201
	else:
		flash('No entries for search parameters!')
	return render_template('search.html', title='Search', form = form)

if __name__ == '__main__':
	app.run()

