# Generated by Django 3.0.4 on 2020-04-02 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Code', '0013_problem_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=300, verbose_name='Note')),
                ('url', models.URLField(max_length=5000, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'My Resources',
                'verbose_name_plural': 'My Resources',
            },
        ),
        migrations.AlterModelOptions(
            name='resourcetag',
            options={'verbose_name': 'Resource Tags', 'verbose_name_plural': 'Resource Tags'},
        ),
    ]
