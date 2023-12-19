from django.contrib import admin
from .models import LessonType, Student, Lesson, Discipline

class LessonTypeAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'discipline',
        'age_range',
        'max_capacity',
        
    )

    ordering = ('discipline',)

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
 
    )

class LessonAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'type',
        'remaining_capacity',
    )

    readonly_fields = ('remaining_capacity',)

    fields = ('students', 
        'remaining_capacity', 
        'date_time', 
        'kit_req', 
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
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Discipline, DisciplineAdmin)