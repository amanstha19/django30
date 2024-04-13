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


      items =[{"name": "shirt", "store_location": "ktm", "price": "1000"},
    {"name": "pants", "store_location": "bkt", "price": "200"},
    {"name": "trousers", "store_location": "lalitpur", "price": "3000"},
      ]



      return render(request, template_name='home/temp_inherit_home.html', context={"name": "jon", "age": 30, "address": "KTM",
                                                                                   "items": items})


def temp_inherit_features(request):

    name = [
            {"name": "shirt ", "description": "100% pure cotton"},
            {"name": "pants", "description": "very good fabric"},

    ]


    return render(request, template_name='home/temp_inherit_features.html', context = { "name": name })



def temp_inherit_pricing(request):
    return render(request, template_name='home/temp_inherit_pricing.html')