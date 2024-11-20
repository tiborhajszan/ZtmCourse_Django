########################################################################################################################
### Django Bootcamp :: Section 07
### Links Application :: Model Class Definitions
########################################################################################################################

### imports
from django.db import models
from django.utils.text import slugify

########################################################################################################################
### link model class
########################################################################################################################
class Link(models.Model):
    """
    Interface to the Link database table.

    Attributes:
    - name: CharField, short link
    - slug: SlugField, unique slug of short link
    - url: URLField, full URL of link
    - clicks: PositiveIntegerField, clicks of short link
    """

    ### attributes: link table fields (columns) ########################################################################
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    url = models.URLField(max_length=200)
    clicks = models.PositiveIntegerField(default=0)

    ### override of str dunder method ##################################################################################
    def __str__(self):
        """
        Overrides the dunder method for string object representation.

        Returns:
        - str, id: name | clicks
        """

        ### method main logic ------------------------------------------------------------------------------------------

        # returning object string representation
        return f"{self.id}: {self.name} | {self.clicks}"
    
    ### override of parent class save method ###########################################################################
    def save(self, *args, **kwargs):
        """
        Overrides the save method of the parent class.
        Slugifies the short link if it does not already have a slug.

        Args:
        - *args, positional arguments
        - **kwargs, keyword arguments
        """

        ### method main logic ------------------------------------------------------------------------------------------

        # missing slug > slugifying short link
        if not self.slug:
            self.slug = slugify(self.name)
        # saving object
        super().save(*args, **kwargs)
    
    ### click counter method ###########################################################################################
    def click(self):
        """
        Increments the clicks of short link then saves the object.
        """

        ### method main logic ------------------------------------------------------------------------------------------

        # incrementing clicks of short link
        self.clicks += 1
        # saving object
        self.save()
