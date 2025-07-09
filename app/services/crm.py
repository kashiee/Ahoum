from flask import Blueprint, request, jsonify
import os

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def receive_booking():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if token != os.getenv("CRM_WEBHOOK_SECRET"):
        return jsonify({"msg": "Unauthorized"}), 403

    data = request.get_json()
    required = ["booking_id", "user", "event", "facilitator_id"]
    if not all(field in data for field in required):
        return jsonify({"msg": "Missing fields"}), 400

    print("CRM received booking:", data)
    return jsonify({"msg": "Received"}), 200
