import requests
from django.conf import settings
from .models import UsdRate

url = settings.CURRENCY_LATEST_URL


def run_api():
    r = requests.get(url)
    j = r.json()
    obj = UsdRate(rate=str(j["rates"]["RUB"]))
    obj.save()

    return j

