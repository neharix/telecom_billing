from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.main, name="home"),
    path("logout/", views.logout_view, name="logout_view"),
    path("search/", views.search),
    path("client/<int:client_id>/", views.about_sub),
    path("get-pack/<int:package_id>/for/<int:client_id>/", views.get_pack),
    path("set-appraisal/<int:appraisal_id>/for/<int:client_id>/", views.set_appraisal),
    path("toggle-service/<int:service_id>/for/<int:client_id>/", views.toggle_service),
]
