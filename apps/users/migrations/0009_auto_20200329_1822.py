# Generated by Django 2.0.5 on 2020-03-29 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200329_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 18, 22, 5, 975931), verbose_name='发送时间'),
        ),
    ]
