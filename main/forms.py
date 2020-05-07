from django import forms
from .models import AddQuote, AddSubscriptionProduct


class QuoteForm(forms.ModelForm):
    class Meta:
        model = AddQuote
        fields = ['quote_no', 'Opportunity_ID', 'customer_name', 'opp_url', 'lead_name', 'term_type', 'Leading_Product', 'penalties', 'managed_services', 'managed_services_rep', 'local_Currency']
        '''widgets = {
            'quote_no': forms.TextInput(attrs={'class': 'form-control'}),
            'Opportunity_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'opp_url': forms.TextInput(attrs={'class': 'form-control'}),
            'lead_name': forms.Select(attrs={'class': 'form-control'}),
            'term_type': forms.Select(attrs={'class': 'form-control'}),
            'Leading_Product': forms.Select(attrs={'class': 'form-control'}),
            'penalties': forms.Select(attrs={'class': 'form-control'}),
            'managed_services': forms.Select(attrs={'class': 'form-control'}),
            'managed_services_rep': forms.Select(attrs={'class': 'form-control'}),
            'local_Currency': forms.Select(attrs={'class': 'form-control'}),
        }'''

        # validations here

# Production Forms


class SubscriptionAddProductForm(forms.ModelForm):
    class Meta:
        model = AddSubscriptionProduct
        fields = ['productName', 'thirdPartyContent', 'quantity', 'units',
                  'salesDisc', 'currency', 'netSales', 'mcv', 'volDiscPrice', 'termYearly',
                  'productType', 'OppId', 'validProductType']
