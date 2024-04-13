from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def helloworld(request):
    return HttpResponse("<h1> HEllow</h1>")



def home(request):
    return render(request, template_name='home/a.html')

def portfolio(request):
    return render(request, template_name='home/index.html')

def temp_inherit_home(request):
    return render(request, template_name='home/temp_inherit_home.html')