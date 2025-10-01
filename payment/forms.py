
from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "FullName"}),
        required=True
    )

    shipping_address1 = forms.CharField(  # ← دقت کن که اینجا حرف کوچک باشه نه Shipping_address1
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Address1"}),
        required=True
    )

    shipping_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Address2"}),
        required=False
    )

    shipping_city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your City"}),
        required=True
    )

    shipping_state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your State"}),
        required=False
    )

    shipping_zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your PostalCode"}),
        required=False
    )

    shipping_county = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your Country"}),
        required=True
    )
    
    shipping_email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
    )

    class Meta:  # ← این باید داخل کلاس ShippingForm باشه
        model = ShippingAddress
        fields = [
            'shipping_full_name',
            'shipping_email',
            'shipping_address1',
            'shipping_address2',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode',
            'shipping_country',
        ]
        exclude = ['user',]
