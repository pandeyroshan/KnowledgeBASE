# Generated by Django 3.0.4 on 2020-04-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Code', '0014_auto_20200403_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Weeks',
                'verbose_name_plural': 'Weeks',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=5000)),
                ('name', models.CharField(max_length=1000)),
                ('done', models.BooleanField(default=False)),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Code.WeekSet')),
            ],
            options={
                'verbose_name': 'TODOs',
                'verbose_name_plural': 'TODOs',
            },
        ),
    ]