# Generated by Django 2.2.1 on 2019-05-16 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0003_auto_20190516_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 15, 43, 44, 717680)),
        ),
        migrations.AlterField(
            model_name='video',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 16, 15, 43, 44, 717711)),
        ),
    ]