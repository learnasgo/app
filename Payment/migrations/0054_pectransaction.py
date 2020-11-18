# Generated by Django 2.2.6 on 2020-11-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0053_auto_20201116_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='PecTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Token', models.BigIntegerField(verbose_name='توکن')),
                ('OrderId', models.BigIntegerField(verbose_name='شماره تراکنش')),
                ('TerminalNo', models.IntegerField(verbose_name='شماره ترمینال')),
                ('RRN', models.BigIntegerField(verbose_name='شماره یکتایی')),
                ('status', models.IntegerField(verbose_name='کد وضعیت')),
                ('HashCardNumber', models.CharField(max_length=127, verbose_name='شماره کارت هش شده خریدار')),
                ('Amount', models.BigIntegerField(verbose_name='هزینه خرید')),
                ('DiscountedAmount', models.BigIntegerField(verbose_name='هزینه با احتساب تخفیف')),
                ('STraceNo', models.CharField(max_length=127)),
            ],
        ),
    ]
