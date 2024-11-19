
### imports
from django.shortcuts import render, get_object_or_404
from .models import JobPosting

### home page view function
def jobs_index(request):
    """
    Renders the home page of Jobs Board, showing all active job postings.

    Args:
    - request: request object

    Returns:
    - rendered view of home page
    """

    # retrieving active job postings from database
    active_jobs = JobPosting.objects.filter(is_active=True)
    # rendering home page with active job postings
    return render(request=request, template_name="S05_JobsBoardApp/index.html", context={"active_jobs": active_jobs})

### detail page view function
def jobs_detail(request, job_id):
    """
    Renders the detail page of a job posting, if the posting is active.

    Args:
    - request: request object
    - job_id: int, id of job posting to be rendered

    Returns:
    - rendered view of detail page
    """

    # retrieving job posting with given id | 404 error if job posting is inactive or not found
    job = get_object_or_404(JobPosting, id=job_id, is_active=True)
    # rendering detail page of job posting
    return render(request=request, template_name="S05_JobsBoardApp/detail.html", context={"job": job})
