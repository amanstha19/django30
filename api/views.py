
from django.http import JsonResponse
from home.models import Student, ClassRoom
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer, StudentModelSerializer, ClassRoomModelSerializer




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


class StudentListAPIView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        # serializer = StudentSerializer(students, many=True)  #serialization
        serializer = StudentModelSerializer(students, many=True)  #serialization
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     print(self.request.data)
    #
    #     name = request.data.get("name")
    #     age = request.data.get("age")
    #     email = request.data.get("email")
    #     address = request.data.get("address")
    #     Student.objects.create(name=name, age=age, email=email, address=address)
    #
    #     return Response({
    #         "message": "student created successfully "
    #     })

    def post(self,  *args, **kwargs):
        serializer = StudentModelSerializer(self.request.data)  #deserialization
        if serializer.is_valid():
            name = serializer.validated_data['name']
            age = serializer.validated_data['age']
            email = serializer.validated_data['email']
            address = serializer.validated_data['address']



            Student.objects.create(name=name, age=age, email=email, address=address)
            return Response({
                "message": "student created successfully "
            })

        return Response({
            "message": "Invalid request "
        })



class StudentListView(ListAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()




class StudentCreateView(CreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()





class StudentUpdateView(UpdateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class StudentDeleteView(DestroyAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class ClassRoomViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset = ClassRoom.objects.all()


class StudentViewSet(ModelViewSet):

    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


