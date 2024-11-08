from django.shortcuts import render, HttpResponse

# Create your views here.

def movies_index(request):
    return HttpResponse("My Favorite Movies")
