# Generated by Django 3.0.5 on 2020-10-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20200804_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, upload_to='static'),
        ),
    ]
