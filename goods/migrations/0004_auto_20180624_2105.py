# Generated by Django 2.0.6 on 2018-06-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_types_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='types',
            name='gender',
        ),
        migrations.AddField(
            model_name='types',
            name='sale',
            field=models.CharField(choices=[('-1', '普通'), ('2', '特价'), ('1', '折扣')], default='-1', max_length=5, verbose_name='是否折扣'),
        ),
    ]
