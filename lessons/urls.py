from django.urls import path
from . import views

urlpatterns = [
    path ('', views.all_lessons, name='all_lessons'),
    path ('<lessonType_id>', views.lesson_detail, name='lesson_detail')
]
