from flask import Blueprint, request, jsonify
from ..models.event import Event
from ..extensions import db
from flask_jwt_extended import jwt_required

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/', methods=['GET'])
def list_events():
    events = Event.query.all()
    return jsonify([{
        'id': e.id,
        'title': e.title,
        'description': e.description,
        'datetime': e.datetime.isoformat(),
        'facilitator_id': e.facilitator_id,
        'type': e.type,
        'rating': e.rating
    } for e in events])

@bp.route('/filter', methods=['GET'])
def filter_events():
    event_type = request.args.get('type')
    rating = request.args.get('rating', type=float)
    query = Event.query
    if event_type:
        query = query.filter_by(type=event_type)
    if rating is not None:
        query = query.filter(Event.rating >= rating)
    events = query.all()
    return jsonify([{
        'id': e.id,
        'title': e.title,
        'description': e.description,
        'datetime': e.datetime.isoformat(),
        'facilitator_id': e.facilitator_id,
        'type': e.type,
        'rating': e.rating
    } for e in events])

@bp.route('/', methods=['POST'])
@jwt_required()
def create_event():
    data = request.get_json()
    event = Event(
        title=data['title'],
        description=data.get('description'),
        datetime=data['datetime'],
        facilitator_id=data['facilitator_id'],
        type=data.get('type'),
        rating=data.get('rating')
    )
    db.session.add(event)
    db.session.commit()
    return jsonify({"msg": "Event created", "event_id": event.id}), 201

@bp.route('/<int:event_id>', methods=['PUT'])
@jwt_required()
def update_event(event_id):
    data = request.get_json()
    event = Event.query.get_or_404(event_id)
    event.title = data.get('title', event.title)
    event.description = data.get('description', event.description)
    event.datetime = data.get('datetime', event.datetime)
    event.facilitator_id = data.get('facilitator_id', event.facilitator_id)
    event.type = data.get('type', event.type)
    event.rating = data.get('rating', event.rating)
    db.session.commit()
    return jsonify({"msg": "Event updated"})

@bp.route('/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify({
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'datetime': event.datetime.isoformat(),
        'facilitator_id': event.facilitator_id,
        'type': event.type,
        'rating': event.rating
    })


@bp.route('/<int:event_id>', methods=['DELETE'])
@jwt_required()
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return jsonify({"msg": "Event deleted successfully"})

