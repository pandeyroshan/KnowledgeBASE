# Generated by Django 3.0.4 on 2020-03-31 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Code', '0003_auto_20200331_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='problem',
            name='short_note',
            field=models.CharField(max_length=50, verbose_name='Short Note'),
        ),
    ]