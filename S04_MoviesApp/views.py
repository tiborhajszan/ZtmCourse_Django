from django.shortcuts import render, HttpResponse

# Create your views here.

def movies_index(request):
    context = {"movies": ["star wars", "harry potter", "lord of the rings", "star trek", "the mission"]}
    return render(request, "S04_MoviesApp/index.html", context)

def movies_about(request):
    return render(request, "S04_MoviesApp/about.html", {})
