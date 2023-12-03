from django.contrib import admin
from .models import LessonType, Student, LiftPass, Lesson, Discipline

class LessonTypeAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'discipline',
        'age_range',
        'max_capacity',
    )

    ordering = ('discipline',)

class LiftPassAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'type',
        'price',
    )

    ordering = ('type',)

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'age',
    )


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'date_time',
        'type',
    )

    ordering = ('date_time',)

class DisciplineAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        
    )

    ordering = ('name',)
    


# Register your models here.
admin.site.register(LessonType, LessonTypeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(LiftPass, LiftPassAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Discipline, DisciplineAdmin)