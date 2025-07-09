
# Security Practices – Ahoum Booking System

## 🔐 Authentication & Access Control

- **JWT Authentication** is used for secure login and access.
- All protected endpoints are wrapped with `@jwt_required()`.
- JWT tokens are signed using a strong secret key and expire based on default settings.

## 🌐 Google OAuth

- Implemented via Flask-Dance and Google's OAuth 2.0.
- Secure client ID and secret are used from environment variables.
- After successful login, the user is registered (if not already) and a JWT is issued.

## 🧑‍🏫 Role-Based Access

- Each user has a role: `user` or `facilitator`.
- Facilitator-only endpoints verify identity and ownership before performing any actions.

## 🔔 CRM Webhook Security

- The webhook receiver validates the presence of a static Bearer token in the `Authorization` header.
- If the token is missing or invalid, the webhook returns `403 Unauthorized`.
- JSON body is validated for required fields (`booking_id`, `user`, `event`, `facilitator_id`).

## ⚠️ Sensitive Configuration

- Environment variables are used for all secrets, such as:
  - `JWT_SECRET_KEY`
  - `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`
  - `CRM_WEBHOOK_SECRET`
- A `.env.example` file is included to guide setup.

## 🧪 CORS Protection

- CORS is enabled and can be restricted to specific origins during deployment.

## ✅ Error Handling

- All APIs return structured JSON error messages with appropriate HTTP status codes.
- Webhook errors are clearly defined for debugging and validation.

---

These practices are designed to protect data integrity, ensure proper authentication, and isolate communication between internal and external systems.
