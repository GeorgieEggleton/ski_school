from django.contrib import admin
from .models import Order, OrderLineItem
import stripe
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    list_display = (
        '__str__',
        'user',
        'dateTimeCreated',
        'order_total'
    )

class OrderLineItemAdmin(admin.ModelAdmin):
    model = OrderLineItem

    list_display = (
        '__str__',
        'order',
    )

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)