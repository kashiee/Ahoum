from ..extensions import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    datetime = db.Column(db.DateTime)
    facilitator_id = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50))
    rating = db.Column(db.Float)