# Ahoum Booking System

A lightweight Flask-based backend for booking sessions and retreats, developed as part of the Ahoum Backend Developer Internship assignment.

---

## 🚀 Features

- 🔐 User authentication with JWT (Sign up & Log in securely)  
- 🌿 Explore a curated list of events and retreats  
- 🛡️ Book events — available only to logged-in users  
- 📆 Access your personal booking history (upcoming & past)  
- 🔔 Instantly notify the facilitator's CRM on each new booking via webhook  
- 🧮 Filter events by type and minimum rating  
- ✍️ Add, update, or manage events via secure endpoints  

---

## 📁 Project Structure

```
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
```

---

## 🔐 Authentication (JWT)

### Register
`POST /auth/register`
```json
{
  "name": "Test User",
  "email": "1@example.com",
  "password": "password123"
}
```

### Login
`POST /auth/login`
```json
{
  "email": "1@example.com",
  "password": "password123"
}
```

_Response:_
```json
{ "access_token": "<JWT>" }
```

---

## 📅 Event APIs

### 🔎 Get All Events
`GET /events/`

### 🔍 Filter Events by Type and Rating
`GET /events/filter?type=Yoga&rating=4.5`

### 🆕 Add a New Event (JWT required)
`POST /events/`
```json
{
  "title": "Yoga Retreat",
  "description": "A peaceful yoga session",
  "datetime": "2025-08-01T10:00:00",
  "facilitator_id": "FAC001",
  "type": "Yoga",
  "rating": 4.9
}
```

### ✏️ Update an Event (JWT required)
`PUT /events/<event_id>`

```json
{
  "title": "Updated Title",
  "rating": 4.7
}
```

### 🔍 Get Event by ID  
`GET /events/<event_id>`  
Retrieve full details of a specific event using its ID.

📥 **Example:**
```http
GET /events/2
```

📤 **Response:**
```json
{
  "id": 2,
  "title": "Mindfulness Session",
  "description": "An hour of guided mindfulness.",
  "datetime": "2025-08-02T17:30:00",
  "facilitator_id": "FAC002",
  "type": "Meditation",
  "rating": 4.5
}
```

---

### 🗑️ Delete an Event (JWT required)  
`DELETE /events/<event_id>`  
Removes an event from the system.

📥 **Example:**
```http
DELETE /events/3
Authorization: Bearer <your_token>
```

📤 **Response:**
```json
{
  "msg": "Event deleted successfully"
}
```

---

## 📝 Booking APIs

### Book an Event (JWT required)
`POST /bookings/`
```json
{ "event_id": 1 }
```

### View My Bookings (JWT required)
`GET /bookings/`

---

## 🔔 CRM Notification

When a booking is made, a POST request is sent to:
```
POST https://example.com/crm-webhook
```
Payload:
```json
{
  "booking_id": 1,
  "user": { "name": "Alice", "email": "alice@example.com" },
  "event_id": 2,
  "facilitator_id": "FAC001"
}
```

---

## 🧪 Quick Test (curl)
```bash
curl -X POST http://127.0.0.1:5000/auth/login   -H "Content-Type: application/json"   -d '{"email": "test@example.com", "password": "password123"}'
```

# 📦 Stripe Integration Guide

To integrate Stripe payments into your Ahoum Booking System, please refer to the full roadmap and implementation guide in the following file:

👉 [stripe_payment_roadmap.md](stripe_payment_roadmap.md)

---

This document includes:
- Stripe library installation
- Setting environment variables
- Creating checkout sessions
- Handling webhooks
- Updating your booking model with payment status

Ensure you have your Stripe test keys ready and follow the steps to connect payments seamlessly.


