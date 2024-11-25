
from django.db import models

# Create your models here.
class ProfileModel(models.Model):

    BG_CHOICES = (
        ("blue", "Blue"),
        ("green", "Green"),
        ("yellow", "Yellow"),)
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    bg_color = models.CharField(max_length=50, choices=BG_CHOICES)

    def __str__(self):
        return self.name

class LinkModel08(models.Model):
    text = models.CharField(max_length=100)
    url = models.URLField()
    profile = models.ForeignKey(to=ProfileModel, on_delete=models.CASCADE, related_name='links')
