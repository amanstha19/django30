from django.urls import path
from .views import add_classroom, add_student,delete_student
urlpatterns = [

    path("add-classroom/", add_classroom, name="add_classroom"),
    path('add-student/', add_student, name='add_student'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),


]