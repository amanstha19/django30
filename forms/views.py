from django.shortcuts import render,redirect
from home.models import ClassRoom

def add_classroom(request):

    if request.method == "POST":
        clas_name = request.POST.get("classname")
        ClassRoom.objects.create(name = clas_name)
        return redirect("add_classroom")


    else:
        classroom = ClassRoom.objects.all()
        return render(request, template_name="forms/classroom.html", context={"classrooms": classroom})





def add_student(request):
    return render( request,template_name='forms/add_student.html')