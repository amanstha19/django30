from django.urls import path 
from .views import helloworld, home, portfolio, temp_inherit_home

urlpatterns = [

    path("", home, name='myhome'),
    path('portfolio/', portfolio, name='portfolio_page'),
    path('temp-inherit/', temp_inherit_home, name='temp_inherit_home')
]

