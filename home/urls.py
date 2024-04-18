from django.urls import path 
from .views import helloworld, home, portfolio, temp_inherit_home, temp_inherit_features, temp_inherit_pricing,student

urlpatterns = [

    path("", home, name='myhome'),
    path('portfolio/', portfolio, name='portfolio_page'),
    path('temp-inherit/', temp_inherit_home, name='temp_inherit_home'),
    path('features/', temp_inherit_features, name='temp_inherit_features'),
    path('pricing/', temp_inherit_pricing, name="temp_inherit_pricing"),
    path('student/', student, name="student"),
]

