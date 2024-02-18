from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.http import require_GET

from .mobile import MOBILE_APPS


@require_GET
@cache_page(60, cache="privacy")
def privacy(request, slug):
    path = settings.BASE_DIR / "privacy" / f"{slug}.html"
    if not path.is_file():
        raise Http404

    with open(path, "r", encoding="utf-8") as f:
        body = f.read()

    context = {
        "title": "Privacy Policy",
        "keywords": "privacy, policy, law, compliance, legal",
        "description": "Detail of the Privacy Policy of the App",
        "body": body,
    }
    return render(request, "core/privacy.html", context)


@require_GET
@cache_page(60, cache="home")
def home(request):
    context = {
        "title": "Apps",
        "apps": MOBILE_APPS,
    }
    return render(request, "core/home.html", context)


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
