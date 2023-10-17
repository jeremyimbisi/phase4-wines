from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class WineType(db.Model):
    __tablename__ = 'wine_types'

    type_id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), nullable=False)

class Region(db.Model):
    __tablename__ = 'regions'

    region_id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(255), nullable=False)

class Varietal(db.Model):
    __tablename__ = 'varietals'

    varietal_id = db.Column(db.Integer, primary_key=True)
    varietal_name = db.Column(db.String(255), nullable=False)

class Wine(db.Model):
    __tablename__ = 'wines'

    wine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('wine_types.type_id'), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('regions.region_id'), nullable=False)
    description = db.Column(db.Text, nullable=True)
    varietal_id = db.Column(db.Integer, db.ForeignKey('varietals.varietal_id'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_rating = db.Column(db.Float, nullable=True)
