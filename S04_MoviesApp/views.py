from django.shortcuts import render, HttpResponse

# Create your views here.

def movies_index(request):
    return render(request, "S04_MoviesApp/index.html", {})

def movies_about(request):
    return render(request, "S04_MoviesApp/about.html", {})
