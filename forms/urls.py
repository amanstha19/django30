from django.urls import path
from .views import add_classroom, add_student
urlpatterns = [

    path("add-classroom/", add_classroom, name="add_classroom"),
    path('add-student/', add_student, name='add_student'),

]