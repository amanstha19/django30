from django.db import models

# Create your models here.

class Student(models.Model):    # class name later becomes table name in database

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)









