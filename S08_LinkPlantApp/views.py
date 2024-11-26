
from django.shortcuts import render
from django.views.generic import ListView
from .models import S08Link

# Create your views here.
class LinkList(ListView):
    model = S08Link
