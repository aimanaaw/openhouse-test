from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length

class NewLog(FlaskForm):
	user_id = StringField('userid',
		validators=[DataRequired(), Length(min = 6, max = 10)])
	session_id = StringField('sessionid',
		validators=[DataRequired(), Length(min = 6, max = 10)])
	time = DateTimeField('date')
	type = StringField('actiontype')
	properties = StringField('jsondata')
	submit = SubmitField('Log Data')

class SearchForm(FlaskForm):
	user_id = StringField('userid',
		validators=[Length(min = 6, max = 10)])
	time = DateTimeField('date')
	type = StringField('actiontype')
	submit = SubmitField('Search Data')
