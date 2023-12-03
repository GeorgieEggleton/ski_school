from django.shortcuts import render, redirect, reverse
from django.contrib import messages

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
   