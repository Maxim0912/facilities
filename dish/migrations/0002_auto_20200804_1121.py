# Generated by Django 3.0.5 on 2020-08-04 11:21

from django.db import migrations

from services.data_pars import get_html, get_nutritives


def parse_data(apps, schema_editor):
    Ingredient = apps.get_model('dish', 'Ingredient')
    results = get_nutritives()
    for iter in results:
        Ingredient.objects.get_or_create(name=iter['name'],
                                         calory=iter['calories'])


class Migration(migrations.Migration):

    dependencies = [
        ('dish', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(parse_data),
    ]