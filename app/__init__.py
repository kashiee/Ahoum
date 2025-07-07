# ahoum-booking-system/app/__init__.py
from flask import Flask
from .extensions import db, jwt
from .routes import auth, events, bookings

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(events.bp)
    app.register_blueprint(bookings.bp)

    return app