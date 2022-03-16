# Generated by Django 4.0.3 on 2022-03-05 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MealCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='images/')),
                ('location', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('is_delivery', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('rating', models.IntegerField()),
                ('meal_category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.mealcategory')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.restaurant')),
            ],
        ),
    ]