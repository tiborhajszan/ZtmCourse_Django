from django.shortcuts import render, get_object_or_404
from .models import JobPosting

# Create your views here.
def jobs_index(request):
    active_jobs = JobPosting.objects.filter(is_active=True)
    context = {"active_jobs": active_jobs}
    return render(request, "S05_JobsBoardApp/index.html", context)

def jobs_detail(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id, is_active=True)
    context = {"job": job}
    return render(request, "S05_JobsBoardApp/detail.html", context)
