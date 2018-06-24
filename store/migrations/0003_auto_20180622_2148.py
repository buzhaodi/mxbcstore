# Generated by Django 2.0.6 on 2018-06-22 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180622_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='companykey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.company', verbose_name='公司'),
        ),
        migrations.AlterField(
            model_name='store',
            name='designerkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='design_name', to=settings.AUTH_USER_MODEL, verbose_name='设计师'),
        ),
        migrations.AlterField(
            model_name='store',
            name='managerkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_name', to=settings.AUTH_USER_MODEL, verbose_name='监理'),
        ),
    ]
