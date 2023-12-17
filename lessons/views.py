from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import LessonType, Lesson


def all_lessons(request):
    query = None
    lessonTypes = LessonType.objects.all()
   
    if request.GET:
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            lessonTypes = lessonTypes.filter() #find all instances of the lessonType pre-filter
            # input in the format [disapline,age,capacity] Ski,,
            try:
                if types[0] != '': # making Django use '' as a whild card rather than  blocking everything
                    lessonTypes = lessonTypes.filter(Q(discipline__name__in=types))                  
                if types[1] != '':
                    lessonTypes = lessonTypes.filter(Q(age_range__in=types))
                if types[2] == 'private':
                    lessonTypes = lessonTypes.filter(Q(max_capacity=1))
                elif types[2] == 'group':
                    lessonTypes = lessonTypes.filter(Q(max_capacity__gt=1))
            except:
                messages.error(request, "invalid search")
                return redirect(reverse('all_lessons'))
            context = {
                'lessontypes' : lessonTypes,
                'discipline' : types[0],
            }
    
        if 'q'in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "you didn't enter anything")
                return redirect(reverse('all_lessons'))
            queries = (Q(discipline__name__icontains=query) | 
                        Q(brief_description__icontains=query) | 
                        Q(age_range__icontains=query) | 
                        Q(level__icontains=query))
            print(queries)
            lessonTypes = lessonTypes.filter(queries)
            context = {
                'lessontypes' : lessonTypes,
                'search_term' : query,
            }
        
    return render(request, 'lessons/lessons.html', context)

def lesson_detail(request, lessonType_id):
    lessons = None
    lessonType = get_object_or_404(LessonType, pk=lessonType_id)
    lessons = Lesson.objects.filter(type__in=lessonType_id)

    context = {
        'lessontype' : lessonType,
        'lessons' : lessons
    }
    
    return render(request, 'lessons/lesson_detail.html', context)


