########################################################################################################################
### Django Bootcamp :: Section 07
### Links Application :: View Definitions
########################################################################################################################

### imports
from django.shortcuts import render
from .models import Link

### links app home page view function ##################################################################################
def links_index(request):
    """
    Renders the home page of Links application.

    Args:
    - request: http request object

    Returns:
    - rendered view of links app home page
    """

    # retrieving all links from database
    links = Link.objects.all()
    # rendering and returning links app home page
    return render(request=request, template_name="S07_LinksApp/index.html", context={"links":links})
