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
        pp = request.FILES.get("pp")
        profile = StudentProfile.objects.create(phone=phone, bio=bio, roll_no=roll, student=student)
        return redirect("student")

        if pp:
            profile.profile_picture = pp
            profile.save()

    else:
        classroom = ClassRoom.objects.all()

        return render(request, template_name='forms/add_student.html', context={"classrooms": classroom})




def delete_student(request, id ):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.delete()
        return redirect("student")
    return render(request, template_name="forms/delete_student.html", context={"student": student})
