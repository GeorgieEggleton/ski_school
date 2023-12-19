from django.conf import settings
from .forms import EmailForm

def signup(request):
    context = {
        'newsletter_form': EmailForm(),
    }
    return context