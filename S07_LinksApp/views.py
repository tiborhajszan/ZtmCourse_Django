########################################################################################################################
### Django Bootcamp :: Section 07
### Links Application :: View Definitions
########################################################################################################################

### imports
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Link
from .forms import LinkForm

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

### links app redirect view function ###################################################################################
def links_redirect(request, link_slug):
    """
    Redirects to the original website.

    Args:
    - request: http request object
    - link_slug: str, slug of short link

    Returns:
    - redirect to original website
    """

    # retrieving link with given slug | 404 error if link is not found
    link = get_object_or_404(Link, slug=link_slug)
    # incrementing clicks of short link
    link.click()
    # redirecting to original website
    return redirect(link.url)

### links app create link form view function ###########################################################################
def links_create(request):
    """
    Renders the create link form of Links application.

    Args:
    - request: http request object

    Returns:
    - links app create link form
    """

    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("links-home"))
        else:
            form = LinkForm()
            data = "Entered data is not valid. Try again!"
    else:
        form = LinkForm()
        data = "Please enter your data!"
    # rendering and returning webform
    return render(request=request, template_name="S07_LinksApp/create.html", context={"form":form, "data":data})
