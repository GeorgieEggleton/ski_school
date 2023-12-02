from django.contrib import admin
from .models import LessonType, Student, LiftPass, Lesson

# Register your models here.
admin.site.register(LessonType)
admin.site.register(Student)
admin.site.register(LiftPass)
admin.site.register(Lesson)
