from django.shortcuts import render, HttpResponse
from .models import JobPosting

# Create your views here.
def jobs_index(request):
    active_jobs = JobPosting.objects.filter(active=True)
    return HttpResponse("<h1>Jobs Board</h1>")
