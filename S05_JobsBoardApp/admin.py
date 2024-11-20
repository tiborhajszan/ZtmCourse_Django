########################################################################################################################
### Django Bootcamp :: Section 06
### Jobs Board Application :: Models Admin Register
########################################################################################################################

### imports
from django.contrib import admin
from .models import JobPosting

### registering job posting model
admin.site.register(JobPosting)
