from __init__ import db


class Gyro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.String(20), nullable=False)
    x_value = db.Column(db.String(20), nullable=False)
    y_value = db.Column(db.String(20), nullable=False)
    z_value = db.Column(db.String(20), nullable=False)
