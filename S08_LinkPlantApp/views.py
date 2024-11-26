
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import S08Link

# Create your views here.
class LinkList(ListView):
    model = S08Link

class LinkCreate(CreateView):
    model = S08Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")
