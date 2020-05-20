from django.db import models
from django.urls import reverse
from django.db.models import Sum


cbd_lead_names = (
    ("Simon Woodford", "Simon Woodford"),
    ("Vin Bolisetti", "Vin Bolisetti"),
)

term_type = (
    ("Cloud Subscription", "Cloud Subscription"),
    ("Cloud Perpetual", "Cloud Perpetual"),
    ("SaaS", "SaaS"),
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
    quote_name = models.CharField(max_length=56, null=True)
    Opportunity_ID = models.CharField(max_length=120)
    customer_name = models.CharField(max_length=120)
    opp_url = models.URLField(max_length=200, help_text='copy and paste SFDC Opportunity URL', null=True, blank=True)
    lead_name = models.CharField(max_length=56, choices=cbd_lead_names)
    term_type = models.CharField(max_length=56, choices=term_type)
    Leading_Product = models.CharField(max_length=120, choices=prod_name)
    penalties = models.CharField(max_length=56, choices=bool_val)
    managed_services = models.CharField(max_length=56, choices=bool_val, null=True)
    managed_services_rep = models.CharField(max_length=56, choices=CDS_rep, null=True)
    local_Currency = models.CharField(max_length=56, choices=currency, null=True)
    perpetualSoftwareOTDirectDiscount = models.IntegerField(default=10)  # change to floats - 7 decimals
    subscriptionSoftwareOTDirectDiscount = models.IntegerField(default=85)  # change to floats - 7 decimals
    perpetualSoftwareThirdPartyDiscount = models.IntegerField(default=5)  # change to floats - 7 decimals
    subscriptionSoftwareThirdPartyDiscount = models.IntegerField(default=30)  # change to floats - 7 decimals

    def __str__(self):
        return f'{self.quote_name} : {self.customer_name}'

    def get_absolute_url(self):
        return reverse("list_quote", kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Add Quotes'


# Production Models

# Products 1

thirdParty = (
    ('No', 'No third party'), ('100%', '100% third party')
)
termYear = (
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)
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
term_type2 = (
    ("Cloud Subscription", "Cloud Subscription"),
    ("Cloud Perpetual", "Cloud Perpetual"),
    ("SaaS", "SaaS"),
)


class AddSubscriptionProduct(models.Model):
    add_quote = models.ForeignKey(AddQuote, on_delete=models.SET_NULL, null=True)
    productName = models.CharField(max_length=128)
    thirdPartyContent = models.CharField(max_length=56, choices=thirdParty)
    quantity = models.IntegerField()
    units = models.CharField(max_length=128)
    salesDisc = models.IntegerField()
    currency = models.CharField(max_length=56, choices=currency2)
    netSales = models.DecimalField(max_digits=13, decimal_places=2)
    mcv = models.FloatField(max_length=128)
    volDiscPrice = models.DecimalField(max_digits=13, decimal_places=2)
    termYearly = models.IntegerField(choices=termYear)
    productType = models.CharField(max_length=128, choices=term_type2)
    OppId = models.CharField(max_length=26)
    thirdPartyBool = models.BooleanField(max_length=6, default=None)
    validProductType = models.BooleanField(default=False)
    ePerpFactor = models.IntegerField(default=49)

    def __str__(self):
        return f'{self.productName} : {self.thirdPartyContent}'

    def get_absolute_url(self):
        return reverse("sub_list", kwargs={"id": self.id})

    def get_new_price(self):
        return self.quantity * self.termYearly

    def get_eq_perp_price(self):
        return (self.volDiscPrice * 100) / self.ePerpFactor


class TestModel1(models.Model):
    mod1Name = models.CharField(max_length=56)
    mod1Num1 = models.IntegerField()
    mod1Num2 = models.IntegerField()
    mod1Bool1 = models.BooleanField()

    def __str__(self):
        return self.mod1Name


class TestModel2(models.Model):
    commonName = models.ForeignKey(TestModel1, on_delete=models.SET_NULL, null=True)
    mod2Name = models.CharField(max_length=56)
    mod2Num1 = models.IntegerField()
    mod2Num2 = models.IntegerField()
    mod2Bool1 = models.BooleanField()

    def __str__(self):
        return self.mod2Name


class SchedulePerpetualModel(models.Model):
    add_quote_sched = models.ForeignKey(AddQuote, on_delete=models.SET_NULL, null=True)
    scheduleName = models.CharField(max_length=128)
    scheduleURL = models.URLField()  # default of 200 length

    def __str__(self):
        return f'{self.add_quote_sched.quote_name} : {self.scheduleName}'

    def get_perpetualSoftwareOTDirectDiscount(self):
        if __name__ == '__main__':
            return self.add_quote_sched.perpetualSoftwareOTDirectDiscount


PROD_TYPE = (
    ('License', 'License'),
    ('Support', 'Support'),
)


class AddPerpetualModel(models.Model):
    add_quote_p = models.ForeignKey(AddQuote, on_delete=models.SET_NULL, null=True)
    add_quote_sched_perp = models.ForeignKey(SchedulePerpetualModel, on_delete=models.SET_NULL, null=True)
    productName_p = models.CharField(max_length=128)
    thirdPartyContent_p = models.CharField(max_length=56, choices=thirdParty)
    quantity_p = models.IntegerField()
    units_p = models.CharField(max_length=128)
    salesDisc_p = models.IntegerField()
    currency_p = models.CharField(max_length=56, choices=currency2)
    netSales_p = models.DecimalField(max_digits=13, decimal_places=2)
    mcv_p = models.FloatField(max_length=128)
    volDiscPrice_p = models.FloatField(max_length=13)
    termMonthly_p = models.IntegerField()
    productType_p = models.CharField(max_length=56, choices=PROD_TYPE)
    OppId_p = models.CharField(max_length=26)

    def get_absolute_url(self):
        return reverse("perpetual_list", kwargs={"id": self.id})

    def get_target_disc_p(self):
        return self.add_quote_p.perpetualSoftwareOTDirectDiscount

    def get_current_disc_p(self):
        return self.salesDisc_p

    def get_revised_net_sales(self):
        return ((100 - self.get_target_disc_p())/100) * float(self.volDiscPrice_p)

    def get_target_disc_third_party_p(self):
        return self.add_quote_p.perpetualSoftwareThirdPartyDiscount

    def get_revised_net_sales_third_party(self):
        return (self.netSales_p/(100 - self.salesDisc_p)) * self.get_target_disc_third_party_p()
