# Generated by Django 2.0.6 on 2018-06-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20180624_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='sellCount',
            field=models.IntegerField(default=0, verbose_name='共售'),
        ),
    ]
