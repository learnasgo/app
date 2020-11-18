# Generated by Django 2.2.6 on 2020-11-16 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0054_pectransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='PecConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.IntegerField(verbose_name='کد وضعیت')),
                ('HashCardNumber', models.CharField(max_length=127, verbose_name='شماره کارت هش شده خریدار')),
                ('Token', models.BigIntegerField(verbose_name='توکن')),
                ('RRN', models.BigIntegerField(verbose_name='شماره یکتایی')),
                ('OrderId', models.BigIntegerField(verbose_name='شماره تراکنش')),
            ],
        ),
    ]
