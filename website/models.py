from . import db

class Mega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(30), unique = True) 
    staff_mvp = db.Column(db.String(30), unique=False) 
    biggest_basket = db.Column(db.Integer, default=None)
    daily_earnings = db.Column(db.Integer, default=None)
    best_seller = db.Column(db.String(30), default=None)
    worst_seller = db.Column(db.String(30), default=None)

class Voids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique = False)
    voids = db.Column(db.Integer, default=None)
    transactions = db.Column(db.Integer, default=None)