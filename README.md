# Ahoum Booking System

A lightweight Flask-based backend for booking sessions and retreats, developed as part of the Ahoum Backend Developer Internship assignment.

---

## 🚀 Features

- 🔐 User authentication with JWT (Sign up & Log in securely)  
- 🌿 Explore a curated list of events and retreats  
- 🛡 Book events — available only to logged-in users  
- 📆 Access your personal booking history (upcoming & past)  
- 🔔 Instantly notify the facilitator's CRM on each new booking via webhook


---

## 📁 Project Structure


/ahoum-booking-system
├── app/
│   ├── models/          # SQLAlchemy models
│   ├── routes/          # API route blueprints
│   ├── services/        # CRM integration
│   ├── extensions.py    # JWT and DB init
│   └── __init__.py      # App factory
├── config.py            # App config
├── run.py               # Entry point
├── seed.py              # DB seeder script
├── requirements.txt     # Dependencies
└── README.md            # Project info



---

## 🔐 Authentication (JWT)

### Register
POST /auth/register
json
{
  "name": "Test User",
  "email": "1@example.com",
  "password": "password123"
}


### Login
POST /auth/login
json
{
  "email": "1@example.com",
  "password": "password123"
}

Response:
json
{ "access_token": "<JWT>" }


---

## 📅 Event APIs

### Get All Events
GET /events/

---

## 📝 Booking APIs

### Book an Event
POST /bookings/
Headers: Authorization: Bearer <token>
json
{ "event_id": 1 }


### View My Bookings
GET /bookings/
Headers: Authorization: Bearer <token>

---

## 🔔 CRM Notification

When a booking is made, a POST request is sent to:

POST https://example.com/crm-webhook

With body:
json
{
  "booking_id": 1,
  "user": { "name": "Alice", "email": "alice@example.com" },
  "event_id": 2,
  "facilitator_id": "FAC001"
}


---

## 🧪 Testing with curl
bash
curl -X POST http://127.0.0.1:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password123"}'


---
