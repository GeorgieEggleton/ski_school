from django.db import models

class LessonType(models.Model):
    discipline = models.CharField(null=False, blank=False, max_length=128)
    ageRange = models.CharField(null=False, blank=False, max_length=128)
    maxCapacity = models.IntegerField(null=False, blank=False, default=0)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, null=False, blank=False, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class LiftPass(models.Model):
    type = models.CharField(max_length=128, null=False, blank=False,)
    price = models.DecimalField(max_digits=6, null=False, blank=False, decimal_places=2)

    def __str__(self):
        return self.name

class Student(models.Model):
    firstName = models.CharField(null=False, blank=False, max_length=128) 
    lastName = models.CharField(null=False, blank=False, max_length=128)
    age = models.IntegerField(null=False, blank=False, default=0)
    #userAccount = models.OneToOanyField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    students = models.ManyToManyField(Student, null=True)
    dateTime = models.DateTimeField()
    kitReq = models.IntegerField(null=True, blank=False, default=0)
    liftPass = models.ForeignKey('LiftPass',null=True, blank=True, on_delete=models.SET_NULL)
    Type = models.ManyToManyField(LessonType)

    def __str__(self):
        return self.name

