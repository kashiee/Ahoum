from ..extensions import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    facilitator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    booking_time = db.Column(db.DateTime, default=datetime.utcnow)
    payment_status = db.Column(db.String(20), default='unpaid')

    # Optional: relationships for convenience
    user = db.relationship('User', foreign_keys=[user_id], backref='bookings')
    event = db.relationship('Event', backref='bookings')
    facilitator = db.relationship('User', foreign_keys=[facilitator_id], backref='facilitated_bookings')
