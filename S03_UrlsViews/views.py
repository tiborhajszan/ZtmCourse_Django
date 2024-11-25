from django.shortcuts import HttpResponse, render

# Create your views here.

def index(request):
    return render(request=request, template_name="S03_UrlsViews/index.html")

def about(request):
    return HttpResponse("My name is Tibor Hajszan<br>Aspiring Django Developer")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}!")

def add(request, num1, num2):
    return HttpResponse(f"{num1} + {num2} = {num1 + num2}")
