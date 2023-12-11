from decimal import Decimal
from django.conf import settings
from lessons.models import Lesson, Student
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.contrib.auth.models import User #imports the User from the Allauth package

def bag_contents(request):

    bag_items = [] #reseting the bag variable
    associated_students_id = []
    total = 0 #setting the bag total price to 0
    bag = request.session.get('bag',{}) #retreaving "bag" from the session
    print(f" bag:  { bag } ")
    associated_students =  Student.objects.filter(userAccount = request.user).values()
    for associated_student in associated_students:
        associated_students_id.append(associated_student['id'])
    
    for lesson_id, lesson_bag_details in bag.items(): 
        if isinstance(lesson_bag_details["quantity"], int):   #checks that lasson_quantity is a number     
            lesson = get_object_or_404(Lesson, pk=lesson_id) #retrieveds the lesson from the database
            if lesson.remaining_capacity < lesson_bag_details["quantity"]: #checks that the lesson quantity does not exceed the capacity
                    lesson_bag_details["quantity"] = lesson.remaining_capacity
            subTotal = lesson_bag_details["quantity"] * lesson.type.price 
            total += subTotal
            booked_students_ids = []
            for student in lesson_bag_details["students"]:
                booked_students_ids.append(get_object_or_404(Student, pk=lesson_id).id)
            booked_students = Student.objects.filter(pk__in= lesson_bag_details["students"]).values()



            print(f" Associ_students:  { associated_students} ") 
            print(f" booked_students:  { booked_students } ") 
            print(f" associated_students:  { [i for i in associated_students if i not in booked_students ] } ")

            
            bag_items.append({
                'lesson_id': lesson_id,
                'lesson_quantity': lesson_bag_details["quantity"],
                'lesson_quantity_range' : [*range(lesson_bag_details["quantity"] - len(booked_students))], #really longwinded way of  getting an unpacked list to allow .html to printa dropdown fo the number of students on the list.  JInija "range"does nto seem to be supported on Django
                'lesson' : lesson,
                'formatted_lessontime' : lesson.date_time.strftime("%H%M on %a %d %m %Y"),
                'formatted_lesson_id' : f' {lesson.date_time.strftime("%y")}-{lesson_id}',
                'subTotal' : subTotal,
                'booked_students' : booked_students,
                'associated_students' :  [i for i in associated_students if i not in booked_students ] ,
            })
    
    context = {
        
        'bag_items' : bag_items,
        'total': total,
    }

    return context