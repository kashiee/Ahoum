from ..extensions import db

class CRMBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, nullable=False, unique=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    event_id = db.Column(db.Integer, nullable=False)
    facilitator_id = db.Column(db.Integer, nullable=False)
    received_at = db.Column(db.DateTime, server_default=db.func.now())
