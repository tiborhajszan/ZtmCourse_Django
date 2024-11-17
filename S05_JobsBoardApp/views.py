from django.shortcuts import render, HttpResponse
from .models import JobPosting

# Create your views here.
def jobs_index(request):
    active_jobs = JobPosting.objects.filter(is_active=True)
    context = {"active_jobs": active_jobs}
    return render(request, "S05_JobsBoardApp/index.html", context)
