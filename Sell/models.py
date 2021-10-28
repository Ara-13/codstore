from django.db import models

class Account(models.Model):
    code = models.IntegerField(primary_key=True)
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
    ('A', 'Available'),
    ('S', 'Sold'),
    )

    status = models.CharField(max_length=1, choices=S, default='A')

    def __str__(self):
        return "Account_{}".format(self.code)
