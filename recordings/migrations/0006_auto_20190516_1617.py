# Generated by Django 2.2.1 on 2019-05-16 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0005_auto_20190516_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 16, 17, 5, 670527)),
        ),
        migrations.AlterField(
            model_name='video',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 16, 17, 5, 670558)),
        ),
    ]