from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('dateTimeCreated', 
                       'order_total',
                       'user', 
                       'stripe_pid')

    fields = ('full_name',
                'email',
                'country',
                'postcode',
                'dateTimeCreated',    
                'order_total',
                'user', 
                'stripe_pid',)

    list_display = ('id',
                    'stripe_pid', 
                    'dateTimeCreated', 
                    'full_name',
                    'order_total',)

    ordering = ('-dateTimeCreated',)

admin.site.register(Order, OrderAdmin)