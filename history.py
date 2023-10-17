from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Adjust the database URI as needed
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    wines = db.relationship('Wine', backref='owner', lazy='dynamic')
    history = db.relationship('History', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

class Wine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    type = db.Column(db.String(64))
    region = db.Column(db.String(64))
    varietal = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, type, region, varietal, user_id):
        self.name = name
        self.type = type
        self.region = region
        self.varietal = varietal
        self.user_id = user_id

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(64))
    wine_id = db.Column(db.Integer, db.ForeignKey('wine.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, action, wine_id, user_id):
        self.action = action
        self.wine_id = wine_id
        self.user_id = user_id

if __name__ == '__main__':
    app.run(debug=True, port=8080)
