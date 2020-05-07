from django.db import models
from django.urls import reverse

cbd_lead_names = (
    ("Simon Woodford", "Simon Woodford"),
    ("Vin Bolisetti", "Vin Bolisetti"),
)

term_type = (
    ("CS", "Cloud Subscription"),
    ("CP", "Cloud Perpetual"),
    ("SS", "SaaS"),
)

prod_name = (
    ('OpenText ContentSuite', 'OpenText ContentSuite'),
    ('OpenText Experience Suite', 'OpenText Experience Suite'),
    ('OpenText Process Suite', 'OpenText Process Suite'),
    ('OpenText Information Exchange Suite', 'OpenText Information Exchange Suite'),
    ('OpenText Discovery Suite', 'OpenText Discovery Suite'),
    ('OpenText Suite for SAP', 'OpenText Suite for SAP'),
    ('OpenText Suite for Oracle', 'OpenText Suite for Oracle'),
    ('OpenText Suite for Microsoft', 'OpenText Suite for Microsoft'),
    ('OpenText Appworks', 'OpenText Appworks'),
    ('OpenText Cloud', 'OpenText Cloud'),
)

bool_val = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

CDS_rep = (
    ('M1', 'CDS Rep 1'),
    ('M2', 'CDS Rep 2'),
    ('M3', 'CDS Rep 3'),
    ('M4', 'CDS Rep 4'),
    ('M5', 'CDS Rep 5')
)

currency = (
    ('AED', 'AED - UAE Dirham'),
    ('CHF', 'CHF - Swiss Franc'),
    ('EUR', 'Euro - EURO'),
    ('GBP', 'GBP - British Pound'),
    ('USD', 'USD - US Dollar'),
    ('RUB', 'RUB - Russian Ruble'),
    ('JPY', 'JPY - Japanese Yen')
)


class AddQuote(models.Model):
    quote_no = models.CharField(max_length=56, null=True)
    Opportunity_ID = models.CharField(max_length=120)
    customer_name = models.CharField(max_length=120)
    opp_url = models.URLField(max_length=200, help_text='copy and paste SFDC Opportunity URL', null=True, blank=True)
    lead_name = models.CharField(max_length=56, choices=cbd_lead_names)
    term_type = models.CharField(max_length=2, choices=term_type)
    Leading_Product = models.CharField(max_length=120, choices=prod_name)
    penalties = models.CharField(max_length=10, choices=bool_val)
    managed_services = models.CharField(max_length=10, choices=bool_val, null=True)
    managed_services_rep = models.CharField(max_length=2, choices=CDS_rep, null=True)
    local_Currency = models.CharField(max_length=3, choices=currency, null=True)

    def __str__(self):
        return f'{self.Opportunity_ID} : {self.customer_name} : {self.lead_name}'

    def get_absolute_url(self):
        return reverse("list_quote", kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Add Quotes'


# Production Models

thirdParty = (
    ('No', 'No third party'), ('100%', '100% third party')
)
termYear = (
    ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')
)
currency2 = (
    ('AED', 'AED - UAE Dirham'),
    ('CHF', 'CHF - Swiss Franc'),
    ('EUR', 'Euro - EURO'),
    ('GBP', 'GBP - British Pound'),
    ('USD', 'USD - US Dollar'),
    ('RUB', 'RUB - Russian Ruble'),
    ('JPY', 'JPY - Japanese Yen')
)


class AddSubscriptionProduct(models.Model):
    productName = models.CharField(max_length=128)
    thirdPartyContent = models.CharField(max_length=4, choices=thirdParty)
    quantity = models.IntegerField(max_length=4)
    units = models.CharField(max_length=128)
    salesDisc = models.IntegerField(max_length=3)
    currency = models.CharField(max_length=3, choices=currency2)
    netSales = models.FloatField(max_length=128)
    mcv = models.FloatField(max_length=128)
    volDiscPrice = models.FloatField(max_length=128)
    termYearly = models.IntegerField(max_length=1, choices=termYear)
    productType = models.CharField(max_length=2, choices=term_type)
    OppId = models.CharField(max_length=26)
    validProductType = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.productName}'

