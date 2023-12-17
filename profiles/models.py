from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField

class Profile(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"

    def create(self, *args, **kwargs):
        self.user = request.user
        
        

