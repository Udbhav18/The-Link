# Generated by Django 4.0 on 2021-12-23 02:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('link_app', '0005_doubt'),
    ]

    operations = [
        migrations.AddField(
            model_name='doubt',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 23, 2, 55, 49, 626563, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
