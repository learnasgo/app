# Generated by Django 2.2.6 on 2020-02-05 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0028_auto_20200131_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factor',
            name='DiscountType',
            field=models.CharField(blank=True, choices=[('0', 'بدون کوپن'), ('1', 'مدیریتی'), ('2', 'حجره ای'), ('3', 'کمپین'), ('4', 'خرید اولی')], default='0', max_length=1, verbose_name='نوع نخفیف'),
        ),
    ]
