# seed.py
from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.event import Event
from datetime import datetime

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Users
    user1 = User(name="Alice Smith", email="alice@example.com")
    user1.set_password("password123")
    user2 = User(name="Bob Johnson", email="bob@example.com")
    user2.set_password("secure456")

    db.session.add_all([user1, user2])

    # Create Events
    event1 = Event(
        title="Yoga Retreat",
        description="A calming yoga session in the hills.",
        datetime=datetime(2025, 8, 1, 9, 0),
        facilitator_id="FAC001"
    )
    event2 = Event(
        title="Mindfulness Session",
        description="An hour of guided mindfulness.",
        datetime=datetime(2025, 8, 2, 17, 30),
        facilitator_id="FAC002"
    )

    db.session.add_all([event1, event2])
    db.session.commit()

    print("✅ Database seeded with sample users and events.")
