
# Ahoum Booking System

A complete Flask-based backend for booking sessions and retreats, created for the Ahoum Backend Developer Internship assignment. It features JWT and Google OAuth authentication, event management, booking system, CRM integration, and secure facilitator controls.

---

## 🚀 Features Overview

- 🔐 **JWT Authentication** – Secure login system for users.
- 🌐 **Google OAuth 2.0** – Seamless social login via Google.
- 📅 **Event Management** – View, filter, create, update events.
- 📖 **Booking System** – Authenticated users can book events.
- 🧑‍🏫 **Facilitator Features** – Manage event bookings and cancellations.
- 🔔 **CRM Notification System** – Sends booking data to an external CRM webhook securely.
- 🛡️ **Security Focused** – Bearer token protection, role-based access, and secure communication.
- 📦 **Deployment-Ready** – Configured for deployment on Render/Heroku.
- 📪 **Webhook Listener App** – A secondary Flask app receives booking updates.
- 🧪 **Postman Compatible** – Can be tested easily via Postman (optional collection).

---

## 🔐 Authentication

### JWT Login
Users can log in via email and receive a JWT token.

**`POST /auth/login`**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

_Response:_
```json
{ "access_token": "<JWT>" }
```

### Google OAuth Login
Google login is available via Flask-Dance.

**Flow:**
1. `GET /auth/google/login` – Redirects to Google for authentication.
2. `GET /auth/google/callback` – Handles the Google response.
3. A new user is created if they don’t already exist.
4. A JWT token is returned in the response.

**How It Works Internally:**
- Google user info is fetched using Google OAuth access token.
- The backend checks if the email exists in the DB.
- If not found, it creates a user and issues a JWT.

---

## 🔔 CRM Webhook Integration

The CRM system is a separate Flask application that listens on:

**`POST /webhook`**

This endpoint is protected using a static Bearer token passed in the `Authorization` header.

**Payload Example:**
```json
{
  "booking_id": 15,
  "user": { "name": "Alice", "email": "alice@example.com" },
  "event": 7,
  "facilitator_id": 3
}
```

**Security:** If the token is invalid or a field is missing, the webhook responds with `403 Unauthorized` or `400 Bad Request`. This ensures only valid requests are processed by the CRM.

---

## 📚 Full API Reference

### 🔐 Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/login` | Login with email/password |
| GET | `/auth/google/login` | Redirect to Google login |
| GET | `/auth/google/callback` | Handle Google OAuth response |

---

### 📅 Events
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/events` | Get all events |
| GET | `/events/filter?type=Yoga&rating=4.5` | Filter by type & rating |
| POST | `/book/<event_id>` | Book an event (JWT) |

---

### 📖 Bookings
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/bookings/` | View logged-in user's bookings |
| POST | `/book/<event_id>` | Book a specific event |

---

### 🧑‍🏫 Facilitator Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/facilitator/registrations/<event_id>` | View users for your session |
| POST | `/facilitator/cancel/<event_id>` | Cancel event and mark all bookings as refunded |

---

### 🔔 CRM Webhook (Separate Flask App)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/webhook` | Receive booking notification from main app |

---

## ⚙️ Environment Variables

`.env.example`:
```
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=jwtsecretkey
DATABASE_URL=sqlite:///data.db
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
CRM_WEBHOOK_SECRET=crmsecrettoken
```

---

## 🛠️ Deployment

1. Add `Procfile`: `web: gunicorn run:app`
2. Push to Heroku or Render
3. Set environment variables in dashboard
4. The webhook app can be deployed separately

---

## 🧪 Test JWT Auth

```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "test@example.com", "password": "password123"}'
```

---


## 📦 Stripe Integration Guide

To integrate Stripe payments into your Ahoum Booking System, please refer to the full roadmap and implementation guide in the following file:

👉 [stripe_payment_roadmap.md](stripe_payment_roadmap.md)

---


