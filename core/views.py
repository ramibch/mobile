from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.http import require_GET

from .mobile import MOBILE_APPS, get_app


def home(request):
    context = {"title": "Apps", "apps": MOBILE_APPS}
    return render(request, "core/home.html", context)


def app_info(request, slug):
    context = get_app(slug).context | {
        "author": "Rami Boutassghount",
        "author_url": "https://ramiboutas.com/bio/",
        "donation_links": {
            "PayPal": "https://www.paypal.com/paypalme/ramiboutas",
            "buymeacoffee.com": "https://www.buymeacoffee.com/ramiboutas",
        },
    }
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
    context = {
        "title": "Privacy Policy",
        "keywords": "privacy, policy, law, compliance, legal",
        "description": "Detail of the Privacy Policy of the App",
        "body": body,
    }
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
