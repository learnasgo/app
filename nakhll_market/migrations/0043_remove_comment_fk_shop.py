# Generated by Django 2.2.6 on 2020-03-06 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0042_message_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='FK_Shop',
        ),
    ]
