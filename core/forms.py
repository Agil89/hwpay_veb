from django import forms
from .models import BusinessRegistration

class BusinessRegistrationForm(forms.ModelForm):
    class Meta:
        model = BusinessRegistration
        fields = [
            'business_type',
            'articles_of_organization',
            'statement_of_information',
            'business_license',
            'business_address',
            'website',
        ]
