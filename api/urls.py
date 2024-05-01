from django.urls import path
from .views import hello_world, student_info, StudentGetAPIView, StudentListAPIView

urlpatterns = [
    path("hello-world/", hello_world),
    path("student-info/", student_info),
    path("student-api/", StudentListAPIView.as_view()),
    path("student-apiview/<int:id>/", StudentGetAPIView.as_view()),

]
