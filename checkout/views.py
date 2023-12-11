from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderLineItem

def checkout(request):
    
    bag = request.session.get('bag', {})

    
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products')) #Prevents people from manually accessing the URL by typing /checkout

    #current_bag = bag_contents(request)
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


