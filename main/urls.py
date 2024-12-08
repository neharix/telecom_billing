from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("logout/", views.logout_view, name="logout_view"),
    path("search-results/", views.search),
]
