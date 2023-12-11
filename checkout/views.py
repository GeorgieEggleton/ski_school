from django.shortcuts import render, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from .models import Order, OrderLineItem
from bag.context import bag_contents

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    print('          not in post       ')

    if request.method == 'POST':
        print(f'          in post       { request.POST.get('first_name') }')
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST.get('first_name'),
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()

        for lesson_id, lesson_bag_details in bag.items(): 
            if isinstance(lesson_bag_details["quantity"], int):   #checks that lesson_quantity is a number     
                lesson = get_object_or_404(Lesson, pk=lesson_id) #retrieveds the lesson from the database
                if lesson.remaining_capacity < lesson_bag_details["quantity"]: #checks that the lesson quantity does not exceed the capacity
                        lesson_bag_details["quantity"] = lesson.remaining_capacity
                subTotal = lesson_bag_details["quantity"] * lesson.type.price 
                total += subTotal
                booked_students_ids = []
                for student in lesson_bag_details["students"]:
                    booked_students_ids.append(get_object_or_404(Student, pk=lesson_id).id)
                booked_students = Student.objects.filter(pk__in= lesson_bag_details["students"]).values()       
                order_line_item = OrderLineItem(
                    order = order,
                    lesson = lessson,
                    students =  booked_students,
                    lineitem_total = subTotal
                )            
        if not bag:
            messages.error(request, "There's nothing in your bag")
            return redirect(reverse('products')) #Prevents people from manually accessing the URL by typing /checkout

    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    #print(intent)

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 
        'Stripe public key is missing. Did you forget to set it in your environment?')
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'intent.client_secret',
    }

    return render(request, template, context)


