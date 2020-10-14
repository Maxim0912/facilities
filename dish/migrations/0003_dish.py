# Generated by Django 3.0.5 on 2020-08-04 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20200804_1120'),
        ('dish', '0002_auto_20200804_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='static')),
                ('calories', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('ingredients', models.ManyToManyField(to='dish.Ingredient')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dish', to='restaurant.Restaurant')),
            ],
        ),
    ]
