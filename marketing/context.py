from django.conf import settings
from .forms import EmailForm

def signup(request):
    context = {
        'form': EmailForm(),
    }
    return context