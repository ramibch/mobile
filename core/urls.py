from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .sitemaps import get_sitemaps

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),
    path(
        "favicon.ico",
        views.favicon,
        name="favicon",
    ),
    path(
        "sitemaps.xml",
        sitemap,
        {"sitemaps": get_sitemaps()},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "<str:slug>/privacy",
        views.privacy,
        name="privacy",
    ),
    path(
        "<str:slug>/app-info",
        views.app_info,
        name="appinfo",
    ),
]
