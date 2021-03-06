# Generated by Django 2.2.6 on 2020-02-22 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0033_auto_20200218_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='CampaingType',
            field=models.CharField(blank=True, choices=[('0', 'بدون کمپین'), ('1', 'تولد'), ('2', 'مناسبتی'), ('3', 'انجمنی'), ('4', 'فروش اولی'), ('5', 'خرید اولی')], default='0', max_length=1, verbose_name='نوع کمپین'),
        ),
        migrations.AddField(
            model_name='factor',
            name='FK_Campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Payment.Campaign', verbose_name='کد کمپین'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='MaximumAmount',
            field=models.CharField(blank=True, default='0', max_length=15, verbose_name='حداکثر مبلغ خرید'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='MinimumAmount',
            field=models.CharField(blank=True, default='0', max_length=15, verbose_name='حداقل مبلغ خرید'),
        ),
        migrations.AlterField(
            model_name='factor',
            name='DiscountType',
            field=models.CharField(blank=True, choices=[('0', 'بدون کوپن'), ('1', 'مدیریتی'), ('2', 'حجره ای')], default='0', max_length=1, verbose_name='نوع نخفیف'),
        ),
    ]
