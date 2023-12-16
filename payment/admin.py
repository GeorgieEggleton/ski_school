from django.contrib import admin
from .models import UserPayment

class UserPaymentAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'app_user',
        'payment_bool',
        'stripe_checkout_id',

    )

    ordering = ('app_user',)

admin.site.register(UserPayment, UserPaymentAdmin)