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

    # Create Events with 'type' and 'rating'
    events = [
        Event(
            title="Yoga Retreat",
            description="A calming yoga session in the hills.",
            datetime=datetime(2025, 8, 1, 9, 0),
            facilitator_id="FAC001",
            type="Yoga",
            rating=4.8
        ),
        Event(
            title="Mindfulness Session",
            description="An hour of guided mindfulness.",
            datetime=datetime(2025, 8, 2, 17, 30),
            facilitator_id="FAC002",
            type="Meditation",
            rating=4.5
        ),
        Event(
            title="Digital Detox Weekend",
            description="Disconnect from screens and reconnect with nature.",
            datetime=datetime(2025, 9, 10, 10, 0),
            facilitator_id="FAC003",
            type="Wellness",
            rating=4.9
        ),
        Event(
            title="Breathwork Workshop",
            description="Learn techniques to manage stress and anxiety.",
            datetime=datetime(2025, 7, 20, 11, 0),
            facilitator_id="FAC004",
            type="Breathwork",
            rating=4.6
        ),
        Event(
            title="Creative Writing Retreat",
            description="Unlock your inner writer in a peaceful environment.",
            datetime=datetime(2025, 10, 5, 14, 0),
            facilitator_id="FAC005",
            type="Creativity",
            rating=4.7
        ),
    ]

    db.session.add_all(events)
    db.session.commit()

    print("✅ Database seeded with sample users and events.")
