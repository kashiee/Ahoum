# 💳 Roadmap to Integrate Stripe Payments in Ahoum Booking System

This guide outlines the steps to integrate Stripe payments into the Flask-based Ahoum Booking System.

---

## ✅ Step 1: Install Stripe Library

```bash
pip install stripe
```

Add to `requirements.txt`:
```
stripe
```

---

## 🔑 Step 2: Set Environment Variables

In your `.env` file or system environment:

```bash
STRIPE_SECRET_KEY=sk_test_xxx
STRIPE_PUBLIC_KEY=pk_test_xxx
STRIPE_WEBHOOK_SECRET=whsec_xxx
```

Update `config.py`:
```python
class Config:
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
    STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET')
```

---

## 💼 Step 3: Create a Checkout Session

Add a route like `/create-checkout-session`:

```python
import stripe
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import Config

stripe.api_key = Config.STRIPE_SECRET_KEY

checkout_bp = Blueprint('checkout', __name__, url_prefix='/payments')

@checkout_bp.route('/create-checkout-session', methods=['POST'])
@jwt_required()
def create_checkout():
    data = request.get_json()
    event_id = data['event_id']
    # Normally you'd fetch event details from DB
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        mode='payment',
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': 'Retreat Booking'},
                'unit_amount': 2000  # price in cents
            },
            'quantity': 1,
        }],
        success_url='https://yourdomain.com/success',
        cancel_url='https://yourdomain.com/cancel',
    )
    return jsonify({'checkout_url': session.url})
```

---

## 📬 Step 4: Handle Stripe Webhooks

Set up a route to listen to Stripe's webhook events:

```python
@checkout_bp.route('/webhook', methods=['POST'])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get('stripe-signature')
    endpoint_secret = Config.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except stripe.error.SignatureVerificationError:
        return "Invalid signature", 400

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # TODO: Update booking as paid

    return '', 200
```

---

## 📝 Step 5: Update Booking Model (Add payment status)

```python
payment_status = db.Column(db.String(20), default='unpaid')
```

Update logic on successful payment in the webhook to mark it as `paid`.

---

## ✅ Done!

Now your booking system supports Stripe payments!