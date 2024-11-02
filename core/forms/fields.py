from django import forms


class STKPushForm(forms.Form):
    phone_number = forms.CharField(max_length=12, label="Phone Number")
    amount = forms.CharField(max_length=255)
