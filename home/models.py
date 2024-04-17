from django.db import models



class ClassRoom(models.Model):
    name = models.CharField(max_length=10)
# Create your models here.




class Student(models.Model):

          # class name later becomes table name in database

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_student",
                               null=True, blank=True)



class StudentProfile(models.Model):

    phone = models.CharField(max_length=14)
    roll_no = models.IntegerField()
















