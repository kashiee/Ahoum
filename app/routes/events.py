# ahoum-booking-system/app/routes/events.py
from flask import Blueprint, jsonify
from ..models.event import Event

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/', methods=['GET'])
def list_events():
    events = Event.query.all()
    return jsonify([{
        'id': e.id,
        'title': e.title,
        'description': e.description,
        'datetime': e.datetime.isoformat(),
        'facilitator_id': e.facilitator_id
    } for e in events])