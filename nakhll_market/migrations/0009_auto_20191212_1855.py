# Generated by Django 2.2.6 on 2019-12-12 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0008_auto_20191206_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='FK_ExceptionPostRange',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='FK_PostRange',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='PostRangeType',
        ),
    ]
