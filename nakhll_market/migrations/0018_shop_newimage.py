# Generated by Django 2.2.6 on 2019-12-22 07:22

from django.db import migrations, models
import nakhll_market.models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0017_auto_20191221_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='NewImage',
            field=models.ImageField(blank=True, null=True, upload_to=nakhll_market.models.PathAndRename('media/Pictures/Markets/SubMarkets/Shops/'), verbose_name='عکس جدید حجره'),
        ),
    ]
