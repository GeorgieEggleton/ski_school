from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404 
from django.contrib import messages 
from lessons.models import LessonType, Lesson, Student 

def view_bag(request): 
    if request.user.is_authenticated:
        return render(request, 'bag/bag.html') 
    else: 
        messages.error(request, f'please log in') 
        return redirect('account_login')

def add_to_bag(request, item_id): 

    """"Adds lessons to the bag checking that the quantity does not exceed the total number of lessons available""" 

    quantity = int(request.POST.get('quantity')) 
    lesson = request.POST.get('selected_lesson') 
    redirect_url = request.POST.get('redirect_url') 
    bag = request.session.get('bag', {}) 
    lesson_whole = get_object_or_404(Lesson, pk=lesson) 

    if lesson in list(bag.keys()): 
        if bag[lesson]["quantity"] + quantity <= lesson_whole.remaining_capacity: 
            bag[lesson]["quantity"] += quantity 
            messages.success(request, f'Added {quantity} place on {lesson_whole}') 
        else: 
            if lesson_whole.remaining_capacity - bag[lesson]["quantity"] == 0:  
                messages.error(request, f'There are no places remaining on {lesson_whole}') 
            else: 
                messages.error(request, f'There are only {lesson_whole.remaining_capacity - bag[lesson]} places remaining on {lesson_whole}') 
    else: 
        bag[lesson] = {"quantity": quantity, 
                        "students" :[] 
                        } 
        messages.success(request, f'Added {lesson} to your bag') 
    
    request.session['bag'] = bag 
    
    return redirect(redirect_url) 

def update_bag(request, lesson_id): 

    """updates the bag whent he quantity of lessons booked has changed"""

    lesson = get_object_or_404(Lesson, pk=lesson_id) 
    bag = request.session.get('bag', {}) 
    quantity = int(request.POST.get('quantity')) 
   
    if quantity > 0: 
        bag[lesson_id]["quantity"] = quantity 
        messages.info(request, f'Changed number of places on {lesson} to {quantity}') 
    else: 
        bag.pop(lesson_id) 
        messages.info(request, f'Removed {lesson}') 

    request.session['bag'] = bag 
    return render(request, 'bag/bag.html') 

def remove_from_bag(request, lesson_id): 

    """ Removes the selected lesson feromt he bag"""

    try: 
        lesson = get_object_or_404(Lesson, pk=lesson_id) 
        bag = request.session.get('bag', {}) 
        bag.pop(lesson_id) 
        messages.info(request, f'Removed {lesson} from your bag') 
        request.session['bag'] = bag 
        return render(request, 'bag/bag.html') 
    except Exception as e: 
        messages.error(request, f'Error removing item; {e}') 
        return render(request, 'bag/bag.html') 

def update_student_pulldown(request): 

    """Changes the available students that can be placed on a single
    course, based on previous user selection."""

    bag = request.session.get('bag', {}) 
    lesson_id = str(request.POST.get('lesson_id')) 
    remove = str(request.POST.get('remove')) 
    previous = request.POST.get('previous') 
    selected_student_id = request.POST.get('selected_student_id') 
    student = get_object_or_404(Student, pk=selected_student_id) 

    if remove == "True": 
        bag[lesson_id]["students"].remove(selected_student_id) 

    else: 
        if lesson_id in list(bag.keys()): 
            if len(bag[lesson_id]["students"]) <= bag[lesson_id]["quantity"]: 
                if selected_student_id not in bag[lesson_id]["students"]: 
                    if previous != None:  
                        bag[lesson_id]["students"].remove(previous) 
                    bag[lesson_id]["students"].append(selected_student_id) 
    request.session['bag'] = bag 
    return render(request, 'bag/bag.html') 
