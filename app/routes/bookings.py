from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.booking import Booking
from ..models.event import Event
from ..models.user import User
from ..extensions import db
from datetime import datetime
from ..services.crm import notify_crm

bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_bookings():
    user_id = int(get_jwt_identity())
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'event_id': b.event_id,
        'booking_time': b.booking_time.isoformat(),
        'payment_status': b.payment_status,
        'facilitator_id': b.facilitator_id
    } for b in bookings])

@bp.route('/', methods=['POST'])
@jwt_required()
def book():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    # Fetch event & facilitator
    event = Event.query.get(data['event_id'])
    if not event:
        return jsonify({"msg": "Event not found"}), 404

    # Create new booking
    booking = Booking(
        user_id=user_id,
        event_id=event.id,
        facilitator_id=event.facilitator_id,  # ✅ auto-filled from event
        booking_time=datetime.utcnow(),
        payment_status="unpaid"
    )

    db.session.add(booking)
    db.session.commit()

    # Notify CRM (already working)
    user = User.query.get(user_id)
    notify_crm(booking.id, user, event)

    return jsonify({"msg": "Booking confirmed", "booking_id": booking.id}), 201
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.booking import Booking
from ..models.event import Event
from ..models.user import User
from ..extensions import db
from datetime import datetime
from ..services.crm import notify_crm

bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_bookings():
    user_id = int(get_jwt_identity())
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'event_id': b.event_id,
        'booking_time': b.booking_time.isoformat(),
        'payment_status': b.payment_status,
        'facilitator_id': b.facilitator_id
    } for b in bookings])

@bp.route('/', methods=['POST'])
@jwt_required()
def book():
    user_id = int(get_jwt_identity())
    data = request.get_json()

    # Fetch event & facilitator
    event = Event.query.get(data['event_id'])
    if not event:
        return jsonify({"msg": "Event not found"}), 404

    # Create new booking
    booking = Booking(
        user_id=user_id,
        event_id=event.id,
        facilitator_id=event.facilitator_id,  # ✅ auto-filled from event
        booking_time=datetime.utcnow(),
        payment_status="unpaid"
    )

    db.session.add(booking)
    db.session.commit()

    # Notify CRM (already working)
    user = User.query.get(user_id)
    notify_crm(booking.id, user, event)

    return jsonify({"msg": "Booking confirmed", "booking_id": booking.id}), 201
