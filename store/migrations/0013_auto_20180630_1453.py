# Generated by Django 2.0.6 on 2018-06-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20180624_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='avatar',
            field=models.ImageField(blank=True, default='image/default.png', null=True, upload_to='image/%Y/%m', verbose_name='店面头像'),
        ),
    ]