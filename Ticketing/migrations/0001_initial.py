# Generated by Django 2.2.6 on 2019-11-06 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('SeenStatus', models.BooleanField(choices=[(True, 'دیده شده'), (False, 'دیده نشده')], default=False, verbose_name='وضعیت بازدید')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
                'ordering': ('ID',),
            },
        ),
        migrations.CreateModel(
            name='Ticketing',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Title', models.CharField(db_index=True, max_length=100, verbose_name='عنوان')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('SeenStatus', models.BooleanField(choices=[(True, 'دیده شده'), (False, 'دیده نشده')], default=False, verbose_name='وضعیت بازدید')),
                ('FK_Importer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Importer_Ticketing', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تیکت',
                'verbose_name_plural': 'تیکت ها',
                'ordering': ('ID',),
            },
        ),
    ]
