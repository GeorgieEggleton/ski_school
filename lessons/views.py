from django.shortcuts import render
from .models import LessonType


def all_lessons(request):
    
    lessonType = LessonType.objects.all()
    print(lessonType)
    context = {
        'lessontype' : lessonType,
    }
    
    return render(request, 'lessons/lessons.html', context)