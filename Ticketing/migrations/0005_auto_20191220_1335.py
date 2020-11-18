# Generated by Django 2.2.6 on 2019-12-20 10:05

import Ticketing.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ticketing', '0004_message_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketingMessage',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('Date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('Image', models.ImageField(blank=True, help_text='عکس مربوط به تیکت خود را اینجا بارگذاری کنید', null=True, upload_to=Ticketing.models.PathAndRename('media/Pictures/Ticketing'), verbose_name='عکس تیکت')),
                ('FK_Importer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Importer_Message', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پیام',
                'verbose_name_plural': 'پیام ها',
                'ordering': ('ID',),
            },
        ),
        migrations.RemoveField(
            model_name='ticketing',
            name='Description',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='ticketingmessage',
            name='FK_Replay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ticketing_Message', to='Ticketing.Ticketing', verbose_name='پاسخ'),
        ),
    ]
