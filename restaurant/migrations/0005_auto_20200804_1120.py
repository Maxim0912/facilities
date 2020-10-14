# Generated by Django 3.0.5 on 2020-08-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20200518_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='avg_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitude',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitude',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
