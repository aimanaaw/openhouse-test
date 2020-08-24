from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField

class NewLog(FlaskForm):
	user_id = StringField('User Id')
	session_id = StringField('Session Id')
	time = DateTimeField('Date')
	type = StringField('Action Type')
	properties = StringField('Json Data')