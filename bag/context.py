from decimal import Decimal
from django.conf import settings
from lessons.models import Lesson
from django.shortcuts import get_object_or_404
from datetime import datetime

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    bag = request.session.get('bag',{})
    
    for lesson_id, lesson_quantity in bag.items():
        if isinstance(lesson_quantity, int):        
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            if lesson.remaining_capacity < lesson_quantity:
                    lesson_quantity = lesson.remaining_capacity
            subTotal = lesson_quantity * lesson.type.price 
            total += subTotal
            bag_items.append({
                'lesson_id': lesson_id,
                'lesson_quantity': lesson_quantity,
                'lesson' : lesson,
                'formatted_lessontime' : lesson.date_time.strftime("%H%M on %a %d %m %Y"),
                'formatted_lesson_id' : f' {lesson.date_time.strftime("%y")}-{lesson_id}',
                'subTotal' : subTotal,
            })

    context = {
        'bag_items' : bag_items,
        'total': total,
    }

    return context