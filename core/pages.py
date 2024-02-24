from django.utils.functional import cached_property

from .mobile import MobileApp


class Page(object):
    def __init__(
        self, title, description=None, keywords=None, app: MobileApp = None, merge=False
    ) -> None:
        self.description = description
        self.app = app

        if app is not None and merge:
            extra_title = " | " + app.title if app.title is not None else ""
            extra_keywords = ", " + app.keywords if app.keywords is not None else ""
            self.title = title + extra_title
            self.keywords = keywords + extra_keywords
        else:
            self.title = title
            self.keywords = keywords

    @cached_property
    def index_url(self):
        return self.app.index_url

    @cached_property
    def info_url(self):
        return self.app.info_url
