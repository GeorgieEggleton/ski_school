from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from payment.models import Order, OrderLineItem
from profiles.models import Profile
from lessons.models import Student, Lesson
from .bagCalc import bag_contents
import stripe
import time
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string



def product_page(request):
	line_items_stripe = []
	if request.user.is_authenticated:
		formatted_bag = bag_contents(request)
		stripe.api_key = settings.STRIPE_SECRET_KEY
		for item in formatted_bag['bag_items']:
			line_items_stripe.append({
					'price' : stripe.Price.create(
						currency="gbp",
						unit_amount=int(item['lesson_type_price']),
						product_data={"name": item['lesson']},
					),
					'quantity' : item['quantity'],
					})
		
		try:
			profile = Profile.objects.get(user=request.user)
		except:
			messages.error(request, f'Please create your user profile')
			return redirect('profiles')
		checkout_session = stripe.checkout.Session.create( #creates the stripe session object which is the root level class https://stripe.com/docs/api/checkout/sessions/object
			payment_method_types = ['card',],
			line_items = line_items_stripe,
			mode = 'payment',
			customer_creation = 'if_required',
			customer_email = request.user.email,
			success_url = "https://" + settings.ALLOWED_HOSTS[0] + '/payment/payment_successful?session_id={CHECKOUT_SESSION_ID}',
			cancel_url = "https://" + settings.ALLOWED_HOSTS[0] + '/payment/payment_cancelled', 
			)
		return redirect(checkout_session.url, code=303)
	else: 
		messages.error(request, f'please log in') 
		return redirect('account_login')
	
def payment_successful(request):
	if request.user.is_authenticated:
		try:
			profile = Profile.objects.get(user=request.user)
		except:
			profile = []
		customer = ''
		stripe.api_key = settings.STRIPE_SECRET_KEY
		checkout_session_id = request.GET.get('session_id', None)
		session = stripe.checkout.Session.retrieve(checkout_session_id)
		order = Order.objects.create(user=request.user)
		order.stripe_pid = checkout_session_id 
		if session["customer_details"]["name"] == '':
			order.full_name = profile.full_name
		else:
			order.full_name = session["customer_details"]["name"]
		order.country = session["customer_details"]["address"]["country"] or ''
		order.postcode = session["customer_details"]["address"]["postal_code"] or ''
		order.email = session["customer_details"]["email"]
		order.order_total = session["amount_total"]/100
		order.save()
		
		formatted_bag = bag_contents(request)
		for item in formatted_bag['bag_items']:
			orderlineitem = OrderLineItem.objects.create(
				order = order,
				lesson = (item['lesson']),
				lineitem_total = (item['subTotal'])
			)
			for booked_student in item['booked_students']:				
				booked_student = Student.objects.get(id=booked_student['id'])
				lesson = Lesson.objects.get(id = item['lesson'].id)
				booked_student.orderlineitem_set.add(orderlineitem)
				if lesson.remaining_capacity > 0: lesson.remaining_capacity -= 1 
				lesson.save()
		
		send_mail(
			subject = render_to_string('payment/confirmation_emails/confirmation_email_subject.txt',
				{'order_number' : order.id}),
			message = render_to_string(
				'payment/confirmation_emails/confirmation_email_text.txt',
				{'bag_contents': formatted_bag,
				'order_number': order.id,
				'stripe_PID' : checkout_session_id,
				'user' :  order.full_name,
				}),
			from_email=settings.EMAIL_HOST_USER,
			recipient_list=[request.user.email],
			)
		
		request.session['bag'] = {}
		messages.success(request, f'Payment Successful an email has been sent to {request.user.email}') 
		return redirect('home')

def payment_cancelled(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY
	messages.error(request, f'Payment failed - please retry or contact customer support')
	return redirect('bag')

@csrf_exempt
def stripe_webhook(request):
	stripe.api_key = settings.STRIPE_SECRET_KEY
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