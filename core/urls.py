from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("favicon.ico", views.favicon, name="favicon"),
    path("<str:slug>/privacy", views.privacy, name="privacy"),
    path("<str:slug>/app-info", views.app_info, name="appinfo"),
]
