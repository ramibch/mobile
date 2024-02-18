from functools import cache


class MobileApp(object):
    def __init__(self, title, slug, download_url=None) -> None:
        self.title = title
        self.slug = slug
        self.download_url = download_url

    def page_url(self):
        return f"/{self.slug}/"


MOBILE_APPS = (
    MobileApp(
        title="Hello",
        slug="dgt",
        download_url="https://ramiboutas.com/mobile/dgt-tests-anteriores/",
    ),
)


@cache
def get_app(slug):
    for app in MOBILE_APPS:
        if app.slug == slug:
            return app
