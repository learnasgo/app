# Generated by Django 2.2.6 on 2020-01-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nakhll_market', '0030_auto_20200118_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='Part',
            field=models.CharField(choices=[('0', 'ایجاد پروفایل'), ('1', 'ویرایش پروفایل'), ('2', 'ایجاد حجره'), ('3', 'ویراش حجره'), ('4', 'ایجاد بنر حجره'), ('5', 'ویرایش بنر حجره'), ('6', 'ایجاد محصول'), ('7', 'ویراش محصول'), ('8', 'ایجاد بنر محصول'), ('9', 'ویراش بنر محصول'), ('10', 'ایجاد ویژگی جدید'), ('11', 'ثبت ویژگی جدید برای محصول'), ('12', 'ثبت سفارش'), ('13', 'لغو سفارش'), ('14', 'ثبت کامنت جدید'), ('15', 'ثبت نقد و بررسی جدید'), ('16', 'ثبت تیکت جدید'), ('17', 'ایجاد ارزش ویژگی جدید'), ('18', 'ثبت انتقاد و پیشنهاد یا شکایت'), ('19', 'لغو فاکتور'), ('20', 'تایید سفارش'), ('21', 'ارسال سفارش'), ('22', 'حذف بنر حجره'), ('23', 'حذف بنر محصول'), ('24', 'حذف ویژگی محصول'), ('25', 'حذف ارزش ویژگی')], default='0', max_length=2, verbose_name='بخش'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='CanselFirstDate',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ اولین لغو سفارش'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='LimitCancellationDate',
            field=models.DateField(blank=True, null=True, verbose_name='تاریخ محدودیت لغو سفارشات'),
        ),
    ]