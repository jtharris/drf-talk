from django.db import models


class Beer(models.Model):
    STYLES = (
        ('PALE_ALE', 'Pale Ale'),
        ('IPA', 'India Pale Ale (IPA)'),
        ('WHEAT', 'Wheat'),
        ('BLONDE', 'Blonde Ale'),
        ('LAGER', 'Lager'),
        ('STOUT', 'Stout'),
        ('PORTER', 'Porter'),
        ('FARM_HOUSE', 'Farm House/Saison'),
        ('AMBER', 'Amber/Red Ale'),
    )

    name = models.CharField(max_length=100)
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    style = models.CharField(max_length=50, choices=STYLES)
