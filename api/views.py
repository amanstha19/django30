
from django.http import JsonResponse
from home.models import Student




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



# def student_info(request):
#     students = Student.objects.get(id=1)
#     return JsonResponse({"name": students.name,
#             "age": students.age,
#             "address": students.address
#                          })
#
