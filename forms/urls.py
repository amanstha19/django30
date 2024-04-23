from django.urls import path
from .views import add_classroom, add_student, delete_student, detail_student
urlpatterns = [

    path("add-classroom/", add_classroom, name="add_classroom"),
    path('add-student/', add_student, name='add_student'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),
    path('detail-student/<int:id>/', detail_student, name='detail_student'),


]