from flask import Blueprint, request, jsonify, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_dance.contrib.google import make_google_blueprint, google
from app.models import User, db
import os

auth = Blueprint('auth', __name__)

google_bp = make_google_blueprint(
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    redirect_to="auth.google_callback"
)

@auth.route("/google/login")
def google_login():
    return redirect(url_for("google.login"))

@auth.route("/google/callback")
def google_callback():
    resp = google.get("/oauth2/v1/userinfo")
    info = resp.json()
    email = info["email"]
    user = User.query.filter_by(email=email).first()
    if not user:
        user = User(email=email, name=info["name"])
        db.session.add(user)
        db.session.commit()
    token = create_access_token(identity={"id": user.id, "role": user.role})
    return jsonify(access_token=token)