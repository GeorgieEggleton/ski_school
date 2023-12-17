from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):

    readonly_fields = ('dateTimeCreated',)

    list_display = (
 
        'user',
    )

    fields = ('user', 'dateTimeCreated', 'full_name',
               'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',)

    ordering = ('full_name',)

admin.site.register(Profile, ProfileAdmin)