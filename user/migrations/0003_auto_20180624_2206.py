# Generated by Django 2.0.6 on 2018-06-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20180622_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=10),
        ),
    ]
