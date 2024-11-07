from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def about(request):
    return HttpResponse("My name is Tibor Hajszan<br>Aspiring Django Developer")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}!")
