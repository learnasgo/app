# Generated by Django 2.2.6 on 2019-11-29 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0006_auto_20191115_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ('id',), 'verbose_name': 'برگه', 'verbose_name_plural': 'برگه ها'},
        ),
        migrations.AddField(
            model_name='product',
            name='FK_ExceptionPostRange',
            field=models.ManyToManyField(blank=True, related_name='Poduct_PostRange_Exception', to='nakhll_market.PostRange', verbose_name='استثناء های محدوده ارسال'),
        ),
        migrations.AddField(
            model_name='product',
            name='FK_PostRange',
            field=models.ManyToManyField(blank=True, related_name='Product_PostRange', to='nakhll_market.PostRange', verbose_name='استان، شهرستان و شهر'),
        ),
        migrations.AddField(
            model_name='product',
            name='FK_SubMarket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_SubMarket', to='nakhll_market.SubMarket', verbose_name='نام راسته'),
        ),
        migrations.AddField(
            model_name='product',
            name='PostRangeType',
            field=models.CharField(choices=[('1', 'سراسر کشور'), ('2', 'استانی'), ('3', 'شهرستانی'), ('4', 'شهری')], default='1', help_text='محدوده ارسال را بر اساس تایپ های مشخص شده، تعیین کنید.', max_length=1, verbose_name='محدوده ارسال محصولات'),
        ),
        migrations.AlterField(
            model_name='pages',
            name='Publish',
            field=models.BooleanField(choices=[(True, 'منتشر شده'), (False, 'پیش نویس')], default=True, verbose_name='وضعیت انتشار'),
        ),
    ]
