# Generated by Django 2.2.6 on 2019-12-24 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0023_auto_20191223_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='FK_Shop',
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='FK_Profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BankAccount_Shop', to='nakhll_market.Profile', verbose_name='نام شخص'),
        ),
    ]
