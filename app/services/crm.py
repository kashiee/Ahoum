from flask import Blueprint, request, jsonify
import os
import requests
from ..extensions import db
from ..models.crm_booking import CRMBooking  # Make sure path is correct

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def receive_booking():
    # 🔐 Authorization Check
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if token != os.getenv("CRM_WEBHOOK_SECRET"):
        return jsonify({"msg": "Unauthorized"}), 403

    # 📦 Payload Validation
    data = request.get_json()
    required = ["booking_id", "user", "event", "facilitator_id"]
    if not data or not all(field in data for field in required):
        return jsonify({"msg": "Missing or invalid fields"}), 400

    try:
        # 🧾 Store Booking Locally in CRM DB
        new_entry = CRMBooking(
            booking_id=data["booking_id"],
            user_name=data["user"]["name"],
            user_email=data["user"]["email"],
            event_id=data["event"],
            facilitator_id=data["facilitator_id"]
        )
        db.session.add(new_entry)
        db.session.commit()

    except Exception as db_error:
        return jsonify({"msg": "Database error", "error": str(db_error)}), 500

    try:
        # 🔄 Forward the request to another Flask server
        forward_url = os.getenv("FORWARD_FLASK_URL")
        forward_token = os.getenv("FORWARD_FLASK_TOKEN", "")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {forward_token}"
        }

        response = requests.post(forward_url, json=data, headers=headers)
        response.raise_for_status()

    except Exception as e:
        return jsonify({
            "msg": "Booking stored locally, but forwarding failed",
            "error": str(e)
        }), 202

    return jsonify({"msg": "Received, stored, and forwarded successfully"}), 200
