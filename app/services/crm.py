# ahoum-booking-system/app/services/crm.py
import requests

def notify_crm(booking_id, user, event):
    payload = {
        "booking_id": booking_id,
        "user": {
            "name": user.name,
            "email": user.email
        },
        "event_id": event.id,
        "facilitator_id": event.facilitator_id
    }
    # Replace with real CRM URL or mock endpoint
    # response = requests.post("https://example.com/crm-webhook", json=payload)
    # return response.status_code