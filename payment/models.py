from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from lessons.models import Lesson, Student
from django.db.models import Sum
import uuid


class Order(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def __str__(self):
        return self.stripe_pid

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    lesson = models.ForeignKey(Lesson, models.SET_NULL, null=True, blank=True)
    students =  models.ManyToManyField(Student, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, default=0)
    

    def __str__(self):
        return f'Lesson {self.lesson} on order {self.order}'