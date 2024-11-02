import base64
from datetime import datetime

import requests
from django.conf import settings

from core.utils.token import AccessToken

access_token = AccessToken().get_token()


class InitiateStkPush:
    def __init__(self):
        ...

    def stk_push(self, phone_number, amount, reference, description):
        try:
            url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" if settings.MPESA_ENVIRONMENT == 'sandbox' else "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": f"Bearer {access_token}"}
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            password = base64.b64encode(
                (settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode('utf-8')).decode('utf-8')

            data = {
                "BusinessShortCode": settings.MPESA_SHORTCODE,
                "Password": password,
                "Timestamp": timestamp,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": amount,
                "PartyA": phone_number,
                "PartyB": settings.MPESA_SHORTCODE,
                "PhoneNumber": phone_number,
                "CallBackURL": settings.MPESA_CALLBACK_URL,
                "AccountReference": reference,
                "TransactionDesc": description,
            }
            response = requests.post(url, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Initiation Error: {e}")
            pass
