# Generated by Django 2.2.6 on 2020-01-30 12:24

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryblog',
            name='DateCreate',
            field=django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ ثبت دسته بندی'),
        ),
        migrations.AlterField(
            model_name='categoryblog',
            name='DateUpdate',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ بروزرسانی دسته بندی'),
        ),
        migrations.AlterField(
            model_name='postblog',
            name='DateCreate',
            field=django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ بارگذاری'),
        ),
        migrations.AlterField(
            model_name='postblog',
            name='DateUpdate',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='postblog',
            name='FK_Shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ShopBlog', to='nakhll_market.Shop', verbose_name='حجره'),
        ),
        migrations.AlterField(
            model_name='vendorstory',
            name='DateCreate',
            field=django_jalali.db.models.jDateField(auto_now_add=True, verbose_name='تاریخ بارگذاری'),
        ),
        migrations.AlterField(
            model_name='vendorstory',
            name='DateUpdate',
            field=django_jalali.db.models.jDateField(auto_now=True, verbose_name='تاریخ بروزرسانی'),
        ),
    ]
