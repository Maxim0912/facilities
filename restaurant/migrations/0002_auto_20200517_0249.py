# Generated by Django 3.0.5 on 2020-05-17 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='adress',
            new_name='adDress',
        ),
    ]
