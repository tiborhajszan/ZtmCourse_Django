
### imports
from django.db import models

### job posting model class
class JobPosting(models.Model):
    """
    Interface to the Job Posting database table.

    Attributes:
    - title: str, job title
    - description: str, job description
    - company: str, company that posted the job
    - salary: int, job salary
    - is_active: bool, True = active posting | False = inactive posting
    """

    ### attributes: job posting table fields (columns)
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)
