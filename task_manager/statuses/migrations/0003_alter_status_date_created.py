# Generated by Django 4.0.4 on 2022-06-27 16:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_status_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 16, 36, 8, 179894, tzinfo=utc), verbose_name='date created'),
        ),
    ]