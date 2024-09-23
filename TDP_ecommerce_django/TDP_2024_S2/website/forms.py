from django import forms
from .models import SellerProduct

class SellerForm(forms.ModelForm):
    class Meta:
        model = SellerProduct
        fields = ['image']