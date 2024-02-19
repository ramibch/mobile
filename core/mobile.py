from functools import cache

from django.urls import reverse_lazy
from django.utils.functional import cached_property


class MobileApp(object):
    def __init__(
        self,
        title,
        slug,
        subtitle=None,
        keywords=None,
        download_url=None,
        free=True,
        extra_context={},  # dynamic way to add more context depending on the app
    ) -> None:
        self.slug = slug
        self.free = free
        self.title = title
        self.subtitle = subtitle
        self.keywords = keywords
        self.download_url = download_url
        self.extra_context = extra_context

    @cached_property
    def page_url(self):
        return f"/{self.slug}/"

    @cached_property
    def info_url(self):
        return reverse_lazy("core-appinfo", {"slug": self.slug})

    @cached_property
    def context(self):
        return {
            "index_url": self.page_url,  # TODO: to use in the navbar (or footer?)
            "title": self.title,
            "description": self.subtitle,
            "keywords": self.keywords,
        } | self.extra_context


MOBILE_APPS = (
    MobileApp(
        title="DGT Test anteriores",
        slug="dgt",
        download_url="https://ramiboutas.com/mobile/dgt-tests-anteriores/",
        extra_context={
            "credits_text": "Los tests de esta aplicación están extraidos de la página oficial de la DGT.",
            "credits_url": "https://revista.dgt.es/",
        },
    ),
)


@cache
def get_app(slug):
    for app in MOBILE_APPS:
        if app.slug == slug:
            return app
