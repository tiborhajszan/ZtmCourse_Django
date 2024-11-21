########################################################################################################################
### Django Bootcamp :: Section 07
### Links Application :: Models Admin Register
########################################################################################################################

### imports
from django.contrib import admin
from .models import Link

### registering link model
admin.site.register(Link)
