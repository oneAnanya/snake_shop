from django.http import HttpResponse
from django.shortcuts import render
from .models import Snake  #from current directory models module import Snake class
# Create your views here.
def sayHello(request):
    return HttpResponse("Hello World") 


def homePage(request):
    snakes = Snake.objects.all()
    return render(request,"shop.html",{"snakes" : snakes})

