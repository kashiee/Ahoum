# Admin/facilitator endpoints
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Event, Booking, db

facilitator = Blueprint("facilitator", __name__)

@facilitator.route("/facilitator/registrations/<int:event_id>")
@jwt_required()
def view_registrations(event_id):
    user = get_jwt_identity()
    event = Event.query.get_or_404(event_id)
    if event.facilitator_id != user["id"]:
        return jsonify(msg="Unauthorized"), 403
    bookings = Booking.query.filter_by(event_id=event.id).all()
    return jsonify([{"user_id": b.user_id, "status": b.status} for b in bookings])

@facilitator.route("/facilitator/cancel/<int:event_id>", methods=["POST"])
@jwt_required()
def cancel_event(event_id):
    user = get_jwt_identity()
    event = Event.query.get_or_404(event_id)
    if event.facilitator_id != user["id"]:
        return jsonify(msg="Unauthorized"), 403
    for b in Booking.query.filter_by(event_id=event_id):
        b.status = "refunded"
    db.session.delete(event)
    db.session.commit()
    return jsonify(msg="Event cancelled and refunds processed")
