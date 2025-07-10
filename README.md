# Ahoum Booking System

A complete Flask-based backend for booking sessions and retreats, created for the Ahoum Backend Developer Internship assignment. It features JWT and Google OAuth authentication, event management, a relational booking system, CRM integration, Stripe payments, and secure facilitator controls.

---

## 🚀 Features Overview

- 🔐 **JWT Authentication** – Secure login system for users.
- 🌐 **Google OAuth 2.0** – Seamless social login via Google.
- 📅 **Event Management** – View, filter, create, update events.
- 📖 **Booking System** – Authenticated users can book events. Bookings are linked to users, events, and facilitators and stored with a `payment_status` for Stripe integration.
- 💳 **Stripe Payments** – Secure payment system with user-event-facilitator metadata handling.
- 🧑‍🏫 **Facilitator Features** – Manage event bookings and cancellations (only for your own events).
- 🔔 **CRM Notification System** – Sends booking data to an external CRM webhook securely.
- 🛡️ **Security Focused** – Bearer token protection, role-based access, secure webhook validation.
- 📦 **Deployment-Ready** – Configured for Render/Heroku with environment variable support.
- 📪 **Webhook Listener App** – A secondary Flask app receives and logs booking updates.
- 🧪 **Postman Compatible** – Easily testable via Postman (optional collection).

---

## 🔐 Authentication

### JWT Login
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

### Google OAuth Login (via Flask-Dance)
**Flow:**
1. `GET /auth/google/login` – Redirects to Google
2. `GET /auth/google/callback` – Handles response
3. New user is auto-created if not found
4. JWT token is returned

---

## 📖 Booking System

Bookings are created by authenticated users. Each booking:
- Links to `user_id`, `event_id`, and `facilitator_id`
- Sets `payment_status = "unpaid"` on creation
- Is marked `"paid"` via Stripe webhook
- Notifies the CRM system with all relational data

---

## 💳 Stripe Integration

Stripe Checkout sessions are created with embedded metadata:

```json
{
  "user_id": 12,
  "event_id": 7,
  "facilitator_id": 3
}
```

This ensures the booking can be traced to the correct user, event, and facilitator upon successful payment confirmation.

👉 For full implementation, see [stripe_payment_roadmap.md](stripe_payment_roadmap.md)

---

## 🔔 CRM Webhook Integration

The CRM system is a separate Flask app that listens on:

**`POST /webhook`**

**Payload Example:**
```json
{
  "booking_id": 15,
  "user": { "name": "Alice", "email": "alice@example.com" },
  "event": 7,
  "facilitator_id": 3
}
```

### 🔐 Security:
- Protected using static Bearer token (`Authorization` header)
- Validates required fields
- Responds with `403` or `400` as needed

### 🗃 Storage & Forwarding:
- ✅ Webhook data is stored in a `CRMBooking` DB table
- ✅ Optionally forwarded to another Flask server
- ✅ Can also mark `Booking` as `"paid"` using `booking_id`, `user_id`, and `event_id`

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
| POST | `/events/` | Create new event |
| PUT | `/events/<event_id>` | Update event |
| DELETE | `/events/<event_id>` | Delete event |

---

### 📖 Bookings
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/bookings/` | View logged-in user's bookings |
| POST | `/bookings/` | Create booking with event_id (includes facilitator ID automatically) |

---

### 🧑‍🏫 Facilitator Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/facilitator/registrations/<event_id>` | View users for your session |
| POST | `/facilitator/cancel/<event_id>` | Cancel your event and mark bookings as refunded |

---

### 🔔 CRM Webhook (Separate Flask App)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/webhook` | Receive booking notification from main app |

---

## 🧑‍💼 Role Management

Each user has a role:
- `"user"` – Can view and book events
- `"facilitator"` – Can manage their own events and view registrations

Role is assigned during registration and enforced via role-based access control.

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
FORWARD_FLASK_URL=http://localhost:6000/receive
FORWARD_FLASK_TOKEN=forwardsecrettoken
STRIPE_SECRET_KEY=your-stripe-secret
STRIPE_WEBHOOK_SECRET=your-stripe-webhook-secret
```

---

## 🛠️ Deployment

1. Add `Procfile`: `web: gunicorn run:app`
2. Push to Heroku or Render
3. Set environment variables in dashboard
4. Deploy webhook app separately if needed

---

## 🧪 Test JWT Auth

```bash
curl -X POST http://localhost:5000/auth/login   -H "Content-Type: application/json"   -d '{"email": "test@example.com", "password": "password123"}'
```# Ahoum Booking System

A complete Flask-based backend for booking sessions and retreats, created for the Ahoum Backend Developer Internship assignment. It features JWT and Google OAuth authentication, event management, a relational booking system, CRM integration, Stripe payments, and secure facilitator controls.

---

## 🚀 Features Overview

- 🔐 **JWT Authentication** – Secure login system for users.
- 🌐 **Google OAuth 2.0** – Seamless social login via Google.
- 📅 **Event Management** – View, filter, create, update events.
- 📖 **Booking System** – Authenticated users can book events. Bookings are linked to users, events, and facilitators and stored with a `payment_status` for Stripe integration.
- 💳 **Stripe Payments** – Secure payment system with user-event-facilitator metadata handling.
- 🧑‍🏫 **Facilitator Features** – Manage event bookings and cancellations (only for your own events).
- 🔔 **CRM Notification System** – Sends booking data to an external CRM webhook securely.
- 🛡️ **Security Focused** – Bearer token protection, role-based access, secure webhook validation.
- 📦 **Deployment-Ready** – Configured for Render/Heroku with environment variable support.
- 📪 **Webhook Listener App** – A secondary Flask app receives and logs booking updates.
- 🧪 **Postman Compatible** – Easily testable via Postman (optional collection).

---

## 🔐 Authentication

### JWT Login
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

### Google OAuth Login (via Flask-Dance)
**Flow:**
1. `GET /auth/google/login` – Redirects to Google
2. `GET /auth/google/callback` – Handles response
3. New user is auto-created if not found
4. JWT token is returned

---

## 📖 Booking System

Bookings are created by authenticated users. Each booking:
- Links to `user_id`, `event_id`, and `facilitator_id`
- Sets `payment_status = "unpaid"` on creation
- Is marked `"paid"` via Stripe webhook
- Notifies the CRM system with all relational data

---

## 💳 Stripe Integration

Stripe Checkout sessions are created with embedded metadata:

```json
{
  "user_id": 12,
  "event_id": 7,
  "facilitator_id": 3
}
```

This ensures the booking can be traced to the correct user, event, and facilitator upon successful payment confirmation.

👉 For full implementation, see [stripe_payment_roadmap.md](stripe_payment_roadmap.md)

---

## 🔔 CRM Webhook Integration

The CRM system is a separate Flask app that listens on:

**`POST /webhook`**

**Payload Example:**
```json
{
  "booking_id": 15,
  "user": { "name": "Alice", "email": "alice@example.com" },
  "event": 7,
  "facilitator_id": 3
}
```

### 🔐 Security:
- Protected using static Bearer token (`Authorization` header)
- Validates required fields
- Responds with `403` or `400` as needed

### 🗃 Storage & Forwarding:
- ✅ Webhook data is stored in a `CRMBooking` DB table
- ✅ Optionally forwarded to another Flask server
- ✅ Can also mark `Booking` as `"paid"` using `booking_id`, `user_id`, and `event_id`

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
| POST | `/events/` | Create new event |
| PUT | `/events/<event_id>` | Update event |
| DELETE | `/events/<event_id>` | Delete event |

---

### 📖 Bookings
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/bookings/` | View logged-in user's bookings |
| POST | `/bookings/` | Create booking with event_id (includes facilitator ID automatically) |

---

### 🧑‍🏫 Facilitator Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/facilitator/registrations/<event_id>` | View users for your session |
| POST | `/facilitator/cancel/<event_id>` | Cancel your event and mark bookings as refunded |

---

### 🔔 CRM Webhook (Separate Flask App)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/webhook` | Receive booking notification from main app |

---

## 🧑‍💼 Role Management

Each user has a role:
- `"user"` – Can view and book events
- `"facilitator"` – Can manage their own events and view registrations

Role is assigned during registration and enforced via role-based access control.

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
FORWARD_FLASK_URL=http://localhost:6000/receive
FORWARD_FLASK_TOKEN=forwardsecrettoken
STRIPE_SECRET_KEY=your-stripe-secret
STRIPE_WEBHOOK_SECRET=your-stripe-webhook-secret
```

---

## 🛠️ Deployment

1. Add `Procfile`: `web: gunicorn run:app`
2. Push to Heroku or Render
3. Set environment variables in dashboard
4. Deploy webhook app separately if needed

---

## 🧪 Test JWT Auth

```bash
curl -X POST http://localhost:5000/auth/login   -H "Content-Type: application/json"   -d '{"email": "test@example.com", "password": "password123"}'
```