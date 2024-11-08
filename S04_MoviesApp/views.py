from django.shortcuts import render, HttpResponse

# Create your views here.

def movies_index(request):
    return render(request, "S04_MoviesApp/index.html", {})
