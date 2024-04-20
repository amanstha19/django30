from django.shortcuts import render, redirect
from home.models import ClassRoom, Student, StudentProfile


def add_classroom(request):
    if request.method == "POST":
        clas_name = request.POST.get("classname")
        ClassRoom.objects.create(name=clas_name)
        return redirect("add_classroom")


    else:
        classroom = ClassRoom.objects.all()
        return render(request, template_name="forms/classroom.html", context={"classrooms": classroom})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom_id")
        student = Student.objects.create(name=name, age=age, email=email, address=address, classroom_id=classroom_id)
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        roll = request.POST.get("roll")
        StudentProfile.objects.create(phone=phone, bio=bio, roll_no=roll, student=student)
        return redirect("student")



    else:
        classroom = ClassRoom.objects.all()

        return render(request, template_name='forms/add_student.html', context={"classrooms": classroom})


