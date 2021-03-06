# Generated by Django 2.2.6 on 2020-01-29 14:46

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nakhll_market', '0032_auto_20200122_2229'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='عنوان دسته بندی')),
                ('Description', models.TextField(blank=True, verbose_name='درباره دسته بندی')),
                ('Image', models.ImageField(blank=True, help_text='عکس دسته بندی را اینجا وارد کنید', null=True, upload_to=blog.models.PathAndRename('media/Pictures/Categories/'), verbose_name='عکس دسته بندی')),
                ('Slug', models.SlugField(unique=True, verbose_name='شناسه دسته بندی')),
                ('DateCreate', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت دسته بندی')),
                ('DateUpdate', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی دسته بندی')),
                ('Publish', models.BooleanField(choices=[(True, 'منتشر شده'), (False, 'در انتظار تایید')], default=False, verbose_name='وضعیت انتشار دسته بندی')),
                ('FK_SubCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SubCategoryBlog', to='blog.CategoryBlog', verbose_name='سر دسته')),
                ('FK_User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Category_Accept_blog', to=settings.AUTH_USER_MODEL, verbose_name='تایید کننده')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ('id', 'Title', 'DateCreate'),
            },
        ),
        migrations.CreateModel(
            name='VendorStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان ')),
                ('Slug', models.SlugField(unique=True, verbose_name='شناسه')),
                ('Content', tinymce.models.HTMLField(verbose_name='متن')),
                ('Summary', models.CharField(blank=True, max_length=400, verbose_name='خلاصه')),
                ('Image', models.ImageField(help_text='عکس محصول خود را اینجا بارگذاری کنید', upload_to=blog.models.PathAndRename('media/Pictures/Markets/SubMarkets/Shops/Products/'), verbose_name='تصویر شاخص')),
                ('Point', models.PositiveIntegerField(default=0, verbose_name='امتیاز')),
                ('DateCreate', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بارگذاری')),
                ('DateUpdate', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('Publish', models.BooleanField(choices=[(True, 'منتشر شده'), (False, 'در انتظار تایید')], default=False, verbose_name='وضعیت انتشار')),
                ('FK_Shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Shop_VendorStory', to='nakhll_market.Shop', verbose_name='حجره')),
                ('FK_User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='VendorStory_Accept', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'داستان حجره دار',
                'verbose_name_plural': 'داستان های حجره دار',
                'ordering': ('DateCreate', 'Title'),
            },
        ),
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان پست ')),
                ('Slug', models.SlugField(unique=True, verbose_name='شناسه پست')),
                ('Content', tinymce.models.HTMLField(verbose_name='متن پست')),
                ('Summary', models.CharField(blank=True, max_length=400, verbose_name='خلاصه')),
                ('Image', models.ImageField(help_text='عکس محصول خود را اینجا بارگذاری کنید', upload_to=blog.models.PathAndRename('media/Pictures/Markets/SubMarkets/Shops/Products/'), verbose_name='تصویر شاخص')),
                ('Point', models.PositiveIntegerField(default=0, verbose_name='امتیاز')),
                ('DateCreate', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بارگذاری')),
                ('DateUpdate', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('Publish', models.BooleanField(choices=[(True, 'منتشر شده'), (False, 'در انتظار تایید')], default=False, verbose_name='وضعیت انتشار')),
                ('FK_Category', models.ManyToManyField(blank=True, related_name='PostCategoryBlog', to='blog.CategoryBlog', verbose_name='دسته بندی های پست')),
                ('FK_Shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ShopBlog', to='nakhll_market.Shop', verbose_name='حجره')),
                ('FK_Tag', models.ManyToManyField(blank=True, related_name='Post_Tag', to='nakhll_market.Tag', verbose_name='تگ ها')),
                ('FK_User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authorPost', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
                'ordering': ('DateCreate', 'Title'),
            },
        ),
    ]
