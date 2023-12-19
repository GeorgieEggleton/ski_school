from django.urls import path
from . import views

urlpatterns = [
	path('', views.profile_creation, name='profiles'),
	path('profile_update/', views.profile_update, name='profile_update'),
	path('order_history/', views.order_history, name='order_history'),
	path ('add_student/', views.add_student, name='add_student'),
	path ('delete_student/<student_id>', views.delete_student, name='delete_student'),
]