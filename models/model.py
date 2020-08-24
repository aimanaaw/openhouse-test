from __main__ import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True, nullable=False)

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.String, primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id


    def __repr__(self):
        return '<id {}>'.format(self.id)


class Action(db.Model):
    __tablename__ = 'actions'

    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    type = db.Column(db.Text)
    properties = db.Column(JSON)
    session_id = db.Column(db.String, db.ForeignKey('sessions.id'))

    def __init__(self,time, type, properties, session_id):
        # self.id = id
        self.time = time
        self.type = type
        self.properties = properties
        self.session_id = session_id

    def __repr__(self):
        return '<id {}>'.format(self.id)