
### imports
from django.shortcuts import render, get_object_or_404
from .models import JobPosting

### home page view
def jobs_index(request):
    """
    Renders the home page of the Jobs Board, with all active job postings.

    Args:
    - request: request object

    Returns:
    - rendered view of the home page
    """

    active_jobs = JobPosting.objects.filter(is_active=True)
    context = {"active_jobs": active_jobs}
    return render(request=request, template_name="S05_JobsBoardApp/index.html", context=context)

### detail page view
def jobs_detail(request, job_id):
    """
    Renders the detail page of a job posting, if the posting is active.

    Args:
    - request: request object
    - job_id: int, id of job posting to be rendered

    Returns:
    - rendered view of the detail page
    """

    job = get_object_or_404(JobPosting, id=job_id, is_active=True)
    context = {"job": job}
    return render(request=request, template_name="S05_JobsBoardApp/detail.html", context=context)
