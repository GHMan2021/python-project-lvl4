# Generated by Django 4.0.4 on 2022-06-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0003_alter_status_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
