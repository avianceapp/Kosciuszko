#1. Build a flask blueprint that charges using stripe using fields set for the cart & the response url redirects to a confirmation page within the route itself.

import stripe
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from prisma.models import User
from libraries.essentials.getenv import get_env

checkout_blueprint = Blueprint('checkout_blueprint', __name__, template_folder='../pages/')

@checkout_blueprint.route('/', methods=['GET','POST'])
def checkout():
    stripe.api_key = get_env('STRIPE_SECRET_KEY')
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Plan.',
                    'images': ['https://i.imgur.com/EHyR2nP.png'],
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:3000/success',
        cancel_url='http://localhost:3000/cancel',
    )
    return redirect(checkout_session.url, code=303)
