from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


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


class Temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    temp_value = db.Column(db.Float, nullable=False)
    humi_value = db.Column(db.Float, nullable=False)


class Current(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    voltage = db.Column(db.Float, nullable=False)
    current = db.Column(db.Float, nullable=False)
    power = db.Column(db.Float, nullable=False)
