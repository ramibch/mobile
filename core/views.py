from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.http import require_GET

from .mobile import get_app
from .pages import Page


def home(request):
    page = Page(
        title=_("Apps"),
        keywords=_("App, App Store, Google, Apple, Google Play, Mobile, Mobile App"),
        description=_("List of all of my developed mobile apps"),
    )
    context = {"page": page}
    return render(request, "core/home.html", context)


def app_info(request, slug):
    context = {"app": get_app(slug)}
    xml_or_html = "xml" if request.hv else "html"
    return render(request, f"core/app_info.{xml_or_html}", context)


@require_GET
@cache_page(3600 * 24 * 30)
def privacy(request, slug):
    path = settings.BASE_DIR / "privacy" / f"{slug}.html"
    if not path.is_file():
        raise Http404
    with open(path, "r", encoding="utf-8") as f:
        body = f.read()

    app = get_app(slug)

    page = Page(
        app=app,
        title=_("Privacy Policy"),
        merge=True,
        keywords=_("privacy, policy, law, compliance, legal"),
        description=_("Detail of the Privacy Policy of the App"),
    )
    context = {"page": page, "body": body}
    return render(request, "core/privacy.html", context)


@require_GET
@cache_control(max_age=60 * 60 * 24 * 30, immutable=True, public=True)  # 30 days
def favicon(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + '<text y=".9em" font-size="90">📱</text>'
            + "</svg>"
        ),
        content_type="image/svg+xml",
    )
