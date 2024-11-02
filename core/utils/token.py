import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth


class AccessToken:
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" if settings.MPESA_ENVIRONMENT == 'sandbox' else "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    def __init__(self):
        ...

    def get_token(self):
        try:
            response = requests.get(self.url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
            response.raise_for_status()
            access_token = response.json().get('access_token')
            return access_token
        except Exception as e:
            print(f"Token Error: {e}")
            pass
