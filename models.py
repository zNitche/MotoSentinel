from __init__ import db


class Gyro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    x_value = db.Column(db.Float, nullable=False)
    y_value = db.Column(db.Float, nullable=False)
    z_value = db.Column(db.Float, nullable=False)


class Accelerometer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    x_value = db.Column(db.Float, nullable=False)
    y_value = db.Column(db.Float, nullable=False)
    z_value = db.Column(db.Float, nullable=False)
