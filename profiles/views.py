from django.shortcuts import render, redirect, get_object_or_404
from payment.models import Order, OrderLineItem
from .forms import Profile_Form
from .models import Profile
from django.contrib import messages

def profile_creation(request):
	profile_form = Profile_Form()
	try:
		profile_name = get_object_or_404(Profile, user=request.user)
		profile_form_entry = {
					'full_name' : profile_name.full_name, 
					'phone_number':profile_name.phone_number,
                  	'street_address1':profile_name.street_address1, 
					'street_address2':profile_name.street_address2,
                  	'town_or_city':profile_name.town_or_city, 
					'postcode':profile_name.postcode, 
					'country':profile_name.country,
                  	'county':profile_name.county,
					}
		profile_form = Profile_Form(profile_form_entry)
		
	finally:
		context = {'Profile_Form' : profile_form}
		return render(request, 'profiles/profile.html', context)


def profile_update(request):

	if request.user.is_authenticated: 
		try:  
			profile = get_object_or_404(Profile, user = request.user)  
		except Profile.DoesNotExist: 
			profile = Profile.objects.create()

			
			
		profile_form_data = Profile_Form(data=request.POST or none, instance = profile)    #allows update of existing profile
		if profile_form_data.is_valid(): 		
			profile = profile_form_data.save(commit=False)
			profile.save()
	else: redirect(account.login)
	context = {'Profile_Form' : profile_form_data}
	return render(request, 'profiles/profile.html', context)
	
def order_history(request):
	orders = []
	full_orders = []
	full_line_item = []
	if request.user.is_authenticated:
		try:  
			orders = Order.objects.filter(user=request.user)
			for order in orders:
				line_items_in_order = order.lineitems.all()
				for line_item_in_order in line_items_in_order:
					full_line_item.append({'lineitem': line_item_in_order, 'students' : line_item_in_order.students.all()})
				full_orders.append({'order': order, 'lineitems': full_line_item })
			print(f"full orders      { full_orders}")
			context = {
				'full_orders' : full_orders,
			}
			
			#print(OrderLineItem.objects.filter(order = orders[0]))
			return render(request, 'profiles/order_history.html', context)
		except Order.DoesNotExist:
			messages.error(request, f"no orders found") 
			return redirect('home')
	else:
		return redirect('account_login')