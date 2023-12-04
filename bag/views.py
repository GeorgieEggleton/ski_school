from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from lessons.models import LessonType, Lesson


def view_bag(request):
    

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    #product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    lesson = request.POST['selected_dates']
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    print(lesson)
    
    
    if lesson in list(bag.keys()):
        bag[lesson] += quantity
        messages.success(request, f'Updated {lesson} quantity to {bag[lesson]}')
    else:
        bag[lesson] = quantity
        messages.success(request, f'Added {lesson} to your bag')
    
    request.session['bag'] = bag
    print( f'Bag: {request.session['bag']}')
    return redirect(redirect_url)

def update_bag(request, lesson_id):

    lesson = get_object_or_404(Lesson, pk=lesson_id)
    bag = request.session.get('bag', {})
    quantity = int(request.POST.get('quantity'))
    print(quantity)
    if quantity > 0:
        bag[lesson_id] = quantity
    else:
        bag.pop(lesson_id)
    request.session['bag'] = bag
    return render(request, 'bag/bag.html')


def remove_from_bag(request, lesson_id):
    
    try:
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        bag = request.session.get('bag', {})
        bag.pop(lesson_id)
        messages.success(request, f'Removed {lesson} from your bag')
        request.session['bag'] = bag
        return render(request, 'bag/bag.html')

    except Exception as e:
        messages.error(request, f'Error removing item; {e}')
        return render(request, 'bag/bag.html')