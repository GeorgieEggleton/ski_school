from django.db import models


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
            type = 'Individual'
        return f"{type} {self.age_range} {self.discipline} lesson"

class LiftPass(models.Model):

    class Meta:
        verbose_name_plural = 'Lift Pass'

    type = models.CharField(max_length=128, null=False, blank=False)
    price = models.DecimalField(max_digits=6, null=False, blank=False, decimal_places=2)

    def __str__(self):
        return self.type

class Student(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=128) 
    last_name = models.CharField(null=False, blank=False, max_length=128)
    age = models.IntegerField(null=False, blank=False, default=0)
    #userAccount = models.OneToManyField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

class Lesson(models.Model):
    students = models.ManyToManyField(Student, blank=True)
    remaining_capacity = models.IntegerField(null=True, blank=False, default=0)
    date_time = models.DateTimeField()
    kit_req = models.IntegerField(null=True, blank=False, default=0)
    lift_pass = models.ForeignKey('LiftPass',null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name="lesson") 


    def __str__(self):
        if self.type.max_capacity > 1:
            type = 'Group'
        else:
            type = 'Individual'

        return f"{self.type.age_range} {type} {self.type.discipline} lesson at {self.date_time.strftime("%H%M on %a %d %B %Y")}"

    """"def __init__(self, *args, **kwargs):
        if self.remaining_capacity == None:
                self.remaining_capacity = self.type.max_capacity
    """

