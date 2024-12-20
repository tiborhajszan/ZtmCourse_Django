"""
URL configuration for Project_Config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from S03_UrlsViews.views import index, about, hello, add
from S04_MoviesApp.views import movies_index, movies_about
from S05_JobsBoardApp.views import jobs_index, jobs_detail
from S07_LinksApp.views import links_index, links_redirect, links_create
from S08_LinkPlantApp.views import LinkList, LinkCreate, LinkUpdate, LinkDelete, plant_profile

urlpatterns = [
    ### site admin url
    path(route="admin/", view=admin.site.urls),

    path("", index),
    path("about/", about),
    path("hello/<str:first_name>/", hello),
    path("add/<int:num1>/<int:num2>/", add),

    path("movies/", movies_index, name="movies-home"),
    path("movies/about/", movies_about, name="movies-about"),
    ### jobs board app urls
    path(route="jobs/", view=jobs_index, name="jobs-home"),
    path(route="jobs/<int:job_id>/", view=jobs_detail, name="jobs-detail"),
    ### links app urls
    path(route="links/", view=links_index, name="links-home"),
    path(route="links/create/", view=links_create, name="links-create"),
    path(route="links/<str:link_slug>/", view=links_redirect, name="links-redirect"),
    ### link plant app urls
    path(route="plant/", view=LinkList.as_view(), name="link-list"),
    path(route="plant/create/", view=LinkCreate.as_view(), name="link-create"),
    path(route="plant/<int:pk>/update/", view=LinkUpdate.as_view(), name="link-update"),
    path(route="plant/<int:pk>/delete/", view=LinkDelete.as_view(), name="link-delete"),
    path(route="plant/<slug:profile_slug>/", view=plant_profile, name="plant-profile"),
]
