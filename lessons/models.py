from django.db import models

class LessonType(models.Model):
    
    class Meta:
        verbose_name_plural = 'Lesson Types'
    
    discipline = models.CharField(null=False, blank=False, max_length=128, help_text='Select Ski or Snowboard')
    age_range = models.CharField(null=False, blank=False, max_length=128)
    max_capacity = models.IntegerField(null=False, blank=False, default=0)
    brief_description = models.TextField(null=True, blank=True, max_length=300)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, null=False, blank=False, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.max_capacity} person capacity  {self.age_range} {self.discipline} lesson"

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
    #userAccount = models.OneToOanyField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

class Lesson(models.Model):
    students = models.ManyToManyField(Student, blank=True)
    date_time = models.DateTimeField()
    kit_req = models.IntegerField(null=True, blank=False, default=0)
    lift_pass = models.ForeignKey('LiftPass',null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name="lesson_type") 

    def __str__(self):
        return f"{self.date_time}  {self.type.discipline}"

