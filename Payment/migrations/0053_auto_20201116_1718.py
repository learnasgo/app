# Generated by Django 2.2.6 on 2020-11-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0052_pecorder_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pecorder',
            name='FactorNumber',
            field=models.CharField(default='0', max_length=10, verbose_name='شماره فاکتور'),
        ),
    ]
