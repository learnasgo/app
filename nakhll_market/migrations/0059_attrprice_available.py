# Generated by Django 2.2.6 on 2020-05-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0058_auto_20200507_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='attrprice',
            name='Available',
            field=models.BooleanField(choices=[(True, 'فعال'), (False, 'غیر فعال')], default=True, verbose_name='وضعیت نمایش ارزش ویژگی محصول'),
        ),
    ]
