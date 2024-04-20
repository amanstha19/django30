from django.db import models



class ClassRoom(models.Model):
    name = models.CharField(max_length=10)
# Create your models here.
    def __str__(self):
        return self.name





class Student(models.Model):
     #one to many foreign key

          # class name later becomes table name in database

    name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_student",
                               null=True, blank=True)
    def __str__(self):
        return self.classroom



class StudentProfile(models.Model):
    #one to one field



    phone = models.CharField(max_length=14)
    roll_no = models.IntegerField()
    bio = models.TextField(max_length=500)
    profile_picture = models.FileField(null=True, blank=True, upload_to="profile_picture")
    student = models.OneToOneField(Student, on_delete=models.CASCADE)




class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline

















