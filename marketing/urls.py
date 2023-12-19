from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.mailchimp_ping_view),
    path('', views.subscribe_view, name='subscribe'),
    path('unsubscribe/', views.unsubscribe_view, name='unsubscribe'),
    path('unsubscribe/success/', views.unsubscribe_success_view, name='unsubscribe-success'),
    path('unsubscribe/fail/', views.unsubscribe_fail_view, name='unsubscribe-fail'),
]