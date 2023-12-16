from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from lessons.models import Lesson, Student

class UserPayment(models.Model):
	app_user = models.ForeignKey(User, on_delete=models.CASCADE)
	payment_bool = models.BooleanField(default=False)
	stripe_checkout_id = models.CharField(max_length=500)

def __str__(self):
	return self.id


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """generates Order Number """
        
        return uuid.uuid4().hex.upper()
    

    def save(self, *args, **kwargs):
        
        """Overwrites save method to calculate total"""

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)


    
    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    lesson = models.ForeignKey(Lesson, models.SET_NULL, null=True, blank=True)
    students =  models.ManyToManyField(Student, blank=True)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False, default=0)

    def post_save(self, *args, **kwargs):
        print(f"students { self.students }")
        self.lineitem_total = self.lesson.type.price
        #self.lineitem_total = self.lesson.type.price * self.students.count()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Lesson {self.lesson} on order {self.order.order_number}'