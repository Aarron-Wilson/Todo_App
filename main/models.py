from django.db import models

class Person(models.Model):
    Name = models.CharField(max_length=30)
    EfficiencyScore = models.DecimalField

class Catagory(models.Model):
    Name = models.CharField(max_length=30)

# Create your models here.
class Todo(models.Model):
    Description = models.CharField(max_length=30)
    Finished = models.BooleanField()
    Catagory = models.ForeignKey(Catagory,on_delete=models.DO_NOTHING)
    AssignedPerson = models.ForeignKey(Person,on_delete=models.DO_NOTHING)