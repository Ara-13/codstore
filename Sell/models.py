from django.db import models
from . import account_code

class Account(models.Model):
    code = models.IntegerField(primary_key=True, blank=True)
    w_code = models.IntegerField(blank=True, null=True)

    level = models.IntegerField()

    region_account = (
    ('220' , '220-هند'),
    ('360' , '360-ایران'),
    ('560' , '560-اروپا')
    )
    region = models.CharField(max_length=3 , choices= region_account, default='360')

    rank = models.CharField(max_length=300, blank=True)

    battle_pass = models.CharField(max_length= 400, blank=True)

    description = models.TextField(blank=True)

    price = models.IntegerField()

    S = (
    ('Available', 'Available'),
    ('Sold', 'Sold'),
    )

    status = models.CharField(max_length=9, choices=S, default='Available')

    S2 = (
    ('w', 'Wait4Publish'),
    ('p', 'Published')
    )

    p_status = models.CharField(max_length=1, choices=S2, default='p')
    def __str__(self):
        return "Account_{}".format(self.code)

class AccountPictures(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank =True, null=True)
    picture = models.ImageField(upload_to="Sell/static/Sell/pictures" , blank=True,  null=True)
    def __str__(self):
        return "Account{}".format(self.account)