from django.db import models

class Account(models.Model):
    code = models.IntegerField(primary_key=True, blank=True)

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

    def __str__(self):
        return "Account_{}".format(self.code)

class AccountPictures(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.CharField(max_length=400)
    straddress = str(address)
    def __str__(self):
        return 'Picture{}'.format(self.account)
