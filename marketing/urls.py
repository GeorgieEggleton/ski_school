from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.mailchimp_ping_view),
    path('', views.subscribe_view, name='subscribe'),
]