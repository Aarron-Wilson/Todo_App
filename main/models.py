from django.db import models

class Person(models.Model):
    Name = models.CharField(max_length=30)
    EfficiencyScore = models.DecimalField

    def __str__(self):
        return self.Name

class Catagory(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

# Create your models here.
class Todo(models.Model):
    Description = models.CharField(max_length=30)
    Finished = models.BooleanField()
    Catagory = models.ForeignKey(Catagory,on_delete=models.DO_NOTHING)
    AssignedPerson = models.ForeignKey(Person,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Description