from django.shortcuts import render, redirect, get_object_or_404
from payment.models import Order, OrderLineItem
from .forms import Profile_Form
from .models import Profile
from lessons.models import Student
from django.contrib import messages

def profile_creation(request):
	
	if request.user.is_authenticated:
		
		profile_form = Profile_Form()
		associated_students = Student.objects.filter(userAccount = request.user)
		try:
			profile_name = Profile.objects.get(user=request.user)  #profile_name = get_object_or_404(Profile, user=request.user)
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
			context = {'Profile_Form' : profile_form,
			'associated_students' : associated_students}
			return render(request, 'profiles/profile.html', context)
	else:
		return redirect('account_login')


def profile_update(request):

	if request.method == 'POST':
		if request.user.is_authenticated:
			try:  
				profile = get_object_or_404(Profile, user = request.user)  
			except:
				profile = Profile.objects.create(user = request.user)	
			profile_form_data = Profile_Form(data=request.POST or none, instance = profile)    #allows update of existing profile
			if profile_form_data.is_valid(): 		
				profile = profile_form_data.save(commit=False)
				profile.save()
			try:  
				associated_students = Student.objects.filter(userAccount = request.user)
			except:
				associated_students = []
		else: 
			messages.error(request, f"Oh dear, you don't seem to be logged in. PLease log in an return") 
			return redirect(account.login)
		context = {
				'Profile_Form' : profile_form_data,
				'associated_students' : associated_students
		}
		return render(request, 'profiles/profile.html', context)
	return redirect(profile_creation)
	
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

			context = {
				'full_orders' : full_orders,
			}
			return render(request, 'profiles/order_history.html', context)
		except Order.DoesNotExist:
			messages.error(request, f"no orders found") 
			return redirect('home')
	else:
		return redirect('account_login')

def add_student(request): 

    studentExists = False 
    redirect_url = request.POST.get('redirect_url')   
    if request.user.is_authenticated:
        linkedStudents = Student.objects.filter(userAccount = request.user).values() #lookup all students associated with login 
        for linkedStudent in linkedStudents: 
            if str(request.POST.get('first_name')) in linkedStudent.values(): 
                if str(request.POST.get('last_name')) in linkedStudent.values(): 
                    messages.error(request, f'Student already exists') 
                    studentExists = True 

        if not studentExists: 
            newstudent = Student.objects.create( 
                first_name = str(request.POST.get('first_name')), 
                last_name = str(request.POST.get('last_name')), 
                dob = request.POST.get('age'), 
                userAccount = request.user 
            )  #creating object from model class 
            newstudent.save() 
            messages.info(request, f'New Student Saved') 

    else: 
        messages.error(request, f'please log in before adding students') 
        return redirect('account_login')

    return redirect(redirect_url)

def delete_student(request, student_id):
	if request.user.is_authenticated:
		if student_id:
			try:
				student = get_object_or_404(Student, id=student_id).delete()
				message.info(request, 'Student Deleted')
			except:
				messages.error(request, 'Unable to delete student')		
			
		return redirect(profile_creation)
	else:
		return redirect('account_login')
