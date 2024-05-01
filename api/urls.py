from django.urls import path
from .views import (hello_world, student_info, StudentGetAPIView,
                    StudentListAPIView, StudentListView, StudentCreateView, StudentUpdateView,StudentDeleteView, ClassRoomViewSet)

from rest_framework.routers import DefaultRouter

# Initialize the router
router = DefaultRouter()

# Register the viewset with the router
router.register('classroom', ClassRoomViewSet)

urlpatterns = [
    path("hello-world/", hello_world),
    path("student-info/", student_info),
    path("student-apiview/", StudentListAPIView.as_view()),
    path("student-apiview/<int:id>/", StudentGetAPIView.as_view()),
]

# Include the router's URLs
urlpatterns += router.urls

generic_urls = [
    path("generic-student-list/", StudentListView.as_view()),
    path("generic-student-create/", StudentCreateView.as_view()),
    path("generic-student-update/<int:pk>/", StudentUpdateView.as_view()),
    path("generic-student-delete/<int:pk>/", StudentDeleteView.as_view())
]

urlpatterns += generic_urls
