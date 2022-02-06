from platform import release
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask.db'
app.config['SQLALCHEMY_SECRET_KEY'] = '123232'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(90), nullable=False)
    email = db.Column(db.String(127), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    albums = db.relationship('Albums', backref='author', lazy=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'{self.first_name}'


class Albums(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    release_date = db.Column(db.String(127), nullable=True,)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'{self.name}'


