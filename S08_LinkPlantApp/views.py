
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profile, S08Link

# Create your views here.
class LinkList(ListView):
    model = S08Link

class LinkCreate(CreateView):
    model = S08Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")

class LinkUpdate(UpdateView):
    model = S08Link
    fields = ["text", "url"]
    success_url = reverse_lazy("link-list")

class LinkDelete(DeleteView):
    model = S08Link
    success_url = reverse_lazy("link-list")

def plant_profile(request, profile_slug):
    context = {
        "profile": get_object_or_404(Profile, slug=profile_slug),
        "links": get_object_or_404(Profile, slug=profile_slug).links.all()}
    return render(request=request, template_name="S08_LinkPlantApp/profile.html", context=context)
