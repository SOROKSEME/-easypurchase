from django import forms

from .models import Customer, ShippingAddress


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "email",
            "company_name",
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "first_name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "last_name"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "email"
            }),
            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "company_name"
            }),
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            "country",
            "address",
            "town",
            "zip_code",
            "phone",
            "comment",
        ]
        widgets = {
            "country": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "countryS"
            }),
            "address": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "addressS"
            }),
            "town": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "townS"
            }),
            "zip_code": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "zip_codeS"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "phoneS"
            }),
            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "commentS"
            })
        }



