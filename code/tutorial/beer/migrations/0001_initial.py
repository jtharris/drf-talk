# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('abv', models.DecimalField(decimal_places=2, max_digits=4)),
                ('style', models.CharField(choices=[('PALE_ALE', 'Pale Ale'), ('IPA', 'India Pale Ale (IPA)'), ('WHEAT', 'Wheat'), ('BLONDE', 'Blonde Ale'), ('LAGER', 'Lager'), ('STOUT', 'Stout'), ('PORTER', 'Porter'), ('FARM_HOUSE', 'Farm House/Saison'), ('AMBER', 'Amber/Red Ale')], max_length=50)),
            ],
        ),
    ]
