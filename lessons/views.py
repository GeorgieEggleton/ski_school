from django.shortcuts import render, get_object_or_404
from .models import LessonType


def all_lessons(request):
    
    lessonTypes = LessonType.objects.all()
    context = {
        'lessontypes' : lessonTypes,
    }
    
    return render(request, 'lessons/lessons.html', context)

def lesson_detail(request, lessonType_id):
    
    lessonType = get_object_or_404(LessonType, pk=lessonType_id)
    print(lessonType)
    
    context = {
        'lessontype' : lessonType,
    }
    
    return render(request, 'lessons/lesson_detail.html', context)
