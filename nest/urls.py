from django.urls import path
from . import views



urlpatterns = [
    path("",views.sayHello),
    path("home",views.homePage)
    
]
