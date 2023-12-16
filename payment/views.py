from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from payment.models import UserPayment
from .bagCalc import bag_contents
import stripe
import time
from django.contrib.auth.models import User
import uuid

def display_product_page(request):
	return render(request, 'payment/product_page.html')

#@login_required(login_url='login')
def product_page(request):
	line_items_stripe = []
	if request.user.is_authenticated:
		formatted_bag = bag_contents(request)
		print(f"formatted bag:      {settings.ALLOWED_HOSTS}")
		stripe.api_key = settings.STRIPE_SECRET_KEY
		"""payment_intent_stripe = stripe.PaymentIntent.create(
								amount=int(formatted_bag['total']),
								currency="gbp",
								automatic_payment_methods={"enabled": True},
								),
		"""
		for item in formatted_bag['bag_items']:
			line_items_stripe.append({
					'price' : stripe.Price.create(
						currency="gbp",
						unit_amount=int(item['lesson_type_price']),
						product_data={"name": item['lesson']},
					),
					'quantity' : item['quantity'],
					})
		
		if request.method == 'POST':
			
			checkout_session = stripe.checkout.Session.create( #creates the stripe session object which is the root level class https://stripe.com/docs/api/checkout/sessions/object
				payment_method_types = ['card'],
				line_items = line_items_stripe,
				mode = 'payment',
				customer_creation = 'always',
				success_url = "https://" + settings.ALLOWED_HOSTS[0] + '/payment/payment_successful?session_id={CHECKOUT_SESSION_ID}',
				cancel_url = "https://" + settings.ALLOWED_HOSTS[0] + '/payment/payment_cancelled', 
				)
			return redirect(checkout_session.url, code=303)
		return render(request, 'payment/product_page.html')

## use Stripe dummy card: 4242 4242 4242 4242
def payment_successful(request):
	
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	checkout_session_id = request.GET.get('session_id', None)
	session = stripe.checkout.Session.retrieve(checkout_session_id)
	customer = stripe.Customer.retrieve(session.customer)
	user_id = request.user.user_id

	
	UserPayment.objects.create(app_user=request.user)
	user_payment = UserPayment.objects.get(app_user=user_id)
	user_payment.stripe_checkout_id = checkout_session_id
	user_payment.save()


	request.session['bag'] = [] 
	return render(request, 'user_payment/payment_successful.html', {'customer': customer})

def payment_cancelled(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	return render(request, 'user_payment/payment_cancelled.html')

@csrf_exempt
def stripe_webhook(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
	time.sleep(10)
	payload = request.body
	signature_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None
	try:
		event = stripe.Webhook.construct_event(
			payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
		)
	except ValueError as e:
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError as e:
		return HttpResponse(status=400)
	if event['type'] == 'checkout.session.completed':
		session = event['data']['object']
		session_id = session.get('id', None)
		time.sleep(15)
		user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
		user_payment.payment_bool = True
		user_payment.save()
	return HttpResponse(status=200)