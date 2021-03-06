# Generated by Django 2.0.6 on 2018-06-24 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180622_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='infos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=50, verbose_name='信息')),
            ],
            options={
                'verbose_name_plural': '门店信息',
            },
        ),
        migrations.CreateModel(
            name='pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='店面照片')),
            ],
            options={
                'verbose_name_plural': '门店照片',
            },
        ),
        migrations.AddField(
            model_name='store',
            name='avatar',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='店面头像'),
        ),
        migrations.AddField(
            model_name='store',
            name='bulletin',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='店面描述'),
        ),
        migrations.AddField(
            model_name='store',
            name='deliveryTime',
            field=models.IntegerField(blank=True, null=True, verbose_name='平均出餐时长'),
        ),
        migrations.AddField(
            model_name='store',
            name='description',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='店面简单描述'),
        ),
        migrations.AddField(
            model_name='store',
            name='foodScore',
            field=models.CharField(default='5', max_length=10, verbose_name='店面评分'),
        ),
        migrations.AddField(
            model_name='store',
            name='minPrice',
            field=models.CharField(default='10', max_length=10, verbose_name='起点价格'),
        ),
        migrations.AddField(
            model_name='store',
            name='name',
            field=models.CharField(default='密雪冰城新店', max_length=50, verbose_name='店名'),
        ),
        migrations.AddField(
            model_name='pics',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store', verbose_name='门店'),
        ),
        migrations.AddField(
            model_name='infos',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Store', verbose_name='门店'),
        ),
    ]
