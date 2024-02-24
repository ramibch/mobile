from django.utils import timezone

from .mobile import APPS


def site(request):
    return {
        "request": request,
        "mobile_apps": APPS,
        "current_year": timezone.now().year,
        "author": "Rami Boutassghount",
        "author_url": "https://ramiboutas.com/bio/",
        "support_links": {
            "Etsy": "https://ramiboutas.etsy.com/",
            "Gumroad": "https://ramiboutas.gumroad.com/",
            "PayPal": "https://www.paypal.com/paypalme/ramiboutas",
            "BuyMeACoffee.com": "https://www.buymeacoffee.com/ramiboutas",
            "GitHub Sponsors": "https://github.com/sponsors/ramiboutas",
        },
        "social_links": {
            "LinkedIn": "https://www.linkedin.com/in/ramiboutas/",
            "GitHub": "https://github.com/ramiboutas/mobile",
            "Twitter": "https://twitter.com/ramiboutas",
            "Mastodon": "https://fosstodon.org/@ramiboutas",
            "Instagram": "https://www.instagram.com/rami_btss/",
        },
        "projects_links": {
            "nicecv.online": "https://www.linkedin.com/in/ramiboutas/",
            "englishstuff.online": "https://github.com/ramiboutas/",
            "ramiboutas.com": "https://ramiboutas.com/",
        },
        "contact_links": {
            "Telegram": "https://t.me/ramiboutas",
            "Email": "mailto:ramiboutas@protonmail.com",
            "WhatsApp": "https://wa.me/+4915752936373",
        },
    }
