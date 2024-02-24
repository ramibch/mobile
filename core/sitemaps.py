from django.contrib.sitemaps import Sitemap

from .mobile import APPS


class AppSitemap(Sitemap):
    changefreq = "never"
    priority = 0.9

    def items(self):
        return APPS


def get_sitemaps():
    sitemaps = {
        "apps": AppSitemap(),
    }
    return sitemaps
