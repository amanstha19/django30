
from django.http import JsonResponse
from home.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer




def hello_world(request):
    return JsonResponse({
        "message": "Hello World "
    })


def student_info(request):
    students = Student.objects.all()
    student_data = []
    for student in students:
        student_data.append({
            "name": student.name,
            "age": student.age,
            "address": student.address
        })
    return JsonResponse(student_data, safe=False)





class StudentGetAPIView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs['id']
        try:
            student = Student.objects.get(id=id)

        except Student.DoesnotExist:
            return Response({
                "detail": "not found"
            })



        serializer = StudentSerializer(student)
        return Response(serializer.data)












