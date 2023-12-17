from django.shortcuts import render, redirect, get_object_or_404

from .forms import Profile_Form
from .models import Profile


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
			print(f"reload {profile.user} {profile.id}")
		except Profile.DoesNotExist: 
			profile = Profile.objects.create()
			print(f"1 {profile.user} {profile.id}")
			
			
		profile_form_data = Profile_Form(data=request.POST or none, instance = profile)    #allows update of existing profile
		if profile_form_data.is_valid(): 		
			profile = profile_form_data.save(commit=False)
			profile.save()
	else: redirect(account.login)
	context = {'Profile_Form' : profile_form_data}
	return render(request, 'profiles/profile.html', context)
	
