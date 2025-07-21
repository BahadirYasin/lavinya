# reservations/forms.py
from django import forms
from .models import WeddingOrganization

class WeddingOrganizationForm(forms.ModelForm):
    class Meta:
        model = WeddingOrganization
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'detail': forms.Textarea(attrs={'rows': 3}),
        }

