from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.conf import settings
from marketing.forms import EmailForm
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import logging

logger = logging.getLogger(__name__)
mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})


def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)

def subscribe_view(request):
    redirect_url = request.POST.get('redirect_url') 
    print(f'in subscribe')
    if request.method == 'POST':
               
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                logger.info(f'API call successful: {response}')
                messages.success(request, f"{ form_email } has been added tot he mailing list")

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                messages.error(request, f"{ form_email } could not be added to the mailing list")

    return redirect(redirect_url) 



def unsubscribe_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            # TODO: use Mailchimp API to unsubscribe
            return redirect('unsubscribe-success')

    return render(request, 'marketing/unsubscribe.html', {
        'form': EmailForm(),
    })


def unsubscribe_success_view(request):
    return render(request, 'marketing/message.html', {
        'title': 'Successfully unsubscribed',
        'message': 'You have been successfully unsubscribed from our mailing list.',
    })


def unsubscribe_fail_view(request):
    return render(request, 'marketing/message.html', {
        'title': 'Failed to unsubscribe',
        'message': 'Oops, something went wrong.',
    })