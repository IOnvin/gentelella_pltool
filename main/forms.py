from django import forms
from .models import AddQuote, AddSubscriptionProduct, TestModel1, TestModel2, AddPerpetualModel, SchedulePerpetualModel


class QuoteForm(forms.ModelForm):
    class Meta:
        model = AddQuote
        fields = ['quote_name', 'Opportunity_ID', 'customer_name', 'opp_url', 'lead_name',
                  'term_type', 'Leading_Product', 'penalties', 'managed_services',
                  'managed_services_rep', 'local_Currency', 'subscriptionSoftwareOTDirectDiscount',
                  'subscriptionSoftwareThirdPartyDiscount', 'perpetualSoftwareOTDirectDiscount',
                  'perpetualSoftwareThirdPartyDiscount']

        '''widgets = {
            'quote_name': forms.TextInput(attrs={'class': 'form-control'}),
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
        fields = ['add_quote', 'productName', 'thirdPartyContent', 'quantity', 'units',
                  'salesDisc', 'currency', 'netSales', 'mcv', 'volDiscPrice', 'termYearly',
                  'productType', 'OppId', 'thirdPartyBool', 'validProductType']


class SchedulePerpetualForm(forms.ModelForm):
    class Meta:
        model = SchedulePerpetualModel
        fields = ['add_quote_sched', 'scheduleName', 'scheduleURL']


class PerpetualAddProductForm(forms.ModelForm):
    class Meta:
        model = AddPerpetualModel
        fields = ['add_quote_p', 'add_quote_sched_perp', 'productName_p', 'thirdPartyContent_p', 'quantity_p', 'units_p',
                  'salesDisc_p', 'currency_p', 'netSales_p', 'mcv_p', 'volDiscPrice_p', 'termMonthly_p',
                  'productType_p', 'OppId_p']


class Test1Form(forms.ModelForm):
    class Meta:
        model = TestModel1
        fields = ['mod1Name', 'mod1Num1', 'mod1Num2', 'mod1Bool1']


class Test2Form(forms.ModelForm):
    class Meta:
        model = TestModel2
        fields = ['commonName', 'mod2Name', 'mod2Num1', 'mod2Num2', 'mod2Bool1']
