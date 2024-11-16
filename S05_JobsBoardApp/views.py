from django.shortcuts import render, HttpResponse

# Create your views here.
def jobs_index(request):
    return HttpResponse("<h1>Jobs Board</h1>")
