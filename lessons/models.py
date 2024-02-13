from django.db import models
from django.contrib.auth.models import User #imports the User from the Allauth package
from django.db.models.signals import post_save
from django.dispatch import receiver

class Discipline(models.Model):
    name = models.CharField(null=False, blank=False, default = 'Ski', max_length=128)
    equipment_type = models.CharField(null=True, blank=True, max_length=128)

    def __str__(self):
        return f"{self.name}"

class LessonType(models.Model):
    
    class Meta:
        verbose_name_plural = 'Lesson Types'
    
    discipline =  models.ForeignKey(Discipline, null = True, on_delete=models.SET_NULL, related_name="lesson_type")
    age_range = models.CharField(null=False, blank=False, max_length=128, choices=[('Child', 'Child'), ('Adult', 'Adult')])
    max_capacity = models.IntegerField(null=False, blank=False, default=0)
    brief_description = models.TextField(null=True, blank=True, max_length=300, default = "")
    description = models.TextField(null=True, blank=True, default = "")
    price = models.DecimalField(max_digits=6, null=False, blank=False, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    level = models.CharField(null=False, blank=False, max_length=128, default = 'unselected', choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])

    def __str__(self):
        if self.max_capacity > 1:
            type = 'Group'
        else:
            type = 'Private'
        return f" {type} {self.age_range} {self.discipline} lesson - {self.level}"

class Student(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=128) 
    last_name = models.CharField(null=False, blank=False, max_length=128)
    dob = models.DateTimeField(blank= True, null = True)
    userAccount = models.ForeignKey(User, null = True, blank = True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}" # - {self.userAccount.email}"

class Lesson(models.Model):
    students = models.ManyToManyField(Student, blank=True)
    remaining_capacity = models.IntegerField(null=True, blank=False, default=0, editable=False)
    date_time = models.DateTimeField(blank= True, null = True)
    kit_req = models.IntegerField(null=True, blank=False, default=0)
    type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name="lesson") 


    
    def save(self, *args, **kwargs):
        

        super().save(*args, **kwargs)
        self.remaining_capacity = self.type.max_capacity - self.students.count()
       
        super().save(*args, **kwargs)
    
    def __str__(self):
        if self.type.max_capacity > 1:
            type = 'Group'
        else:
            type = 'Private'

        return f"{self.type.age_range} {type} {self.type.discipline} lesson at {self.date_time.strftime("%H%M on %a %d %B %Y")}"


