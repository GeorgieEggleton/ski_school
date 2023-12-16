from django.shortcuts import render, redirect

from .forms import Profile_Form



def profile_creation(request):

	try:
		profile_name = get_object_or_404(Lesson, pk=lesson_id)
		profile_form_entry = {
					'full_name' : profile_name.full_name, 
					'email':profile_name.email, 
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
		return render(request, 'profiles/profile.html')


def profile_edit(request):
	return render(request, 'payment/product_page.html')
