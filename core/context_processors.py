from django.utils import timezone

from .mobile import MOBILE_APPS


def site(request):
    return {
        "request": request,
        "mobile_apps": MOBILE_APPS,
        "current_year": timezone.now().year,
        "author": "Rami Boutassghount",
        "author_url": "https://ramiboutas.com/bio/",
        "donation_links": {
            "PayPal": "https://www.paypal.com/paypalme/ramiboutas",
            "BuyMeACoffee.com": "https://www.buymeacoffee.com/ramiboutas",
            "GitHub Sponsors": "https://github.com/sponsors/ramiboutas",
        },
        "social_links": {
            "LinkedIn": "https://www.linkedin.com/in/ramiboutas/",
            "GitHub": "https://github.com/ramiboutas/",
            "Twitter": "https://twitter.com/ramiboutas",
        },
        "projects_links": {
            "nicecv.online": "https://www.linkedin.com/in/ramiboutas/",
            "englishstuff.online": "https://github.com/ramiboutas/",
            "ramiboutas.com": "https://ramiboutas.com/",
        },
    }
