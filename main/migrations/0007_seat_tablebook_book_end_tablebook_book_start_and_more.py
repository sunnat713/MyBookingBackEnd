# Generated by Django 4.0.3 on 2022-03-15 08:50

import config.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_alter_foodbook_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name_uz', models.CharField(max_length=120, null=True)),
                ('name_ru', models.CharField(max_length=120, null=True)),
                ('name_en', models.CharField(max_length=120, null=True)),
                ('desc', models.TextField(blank=True, max_length=1000, null=True)),
                ('amount_seats', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tablebook',
            name='book_end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tablebook',
            name='book_start',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tablebook',
            name='number_of_people',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='tablebook',
            name='status',
            field=models.CharField(choices=[('1', 'Done'), ('2', 'Not yet'), ('3', 'Doing')], default='2', max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='tablebook',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='foodbook',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(null=True, upload_to=config.helpers.UploadTo('restaurant/logo')),
        ),
        migrations.AlterField(
            model_name='restaurantcategory',
            name='icon',
            field=models.ImageField(upload_to=config.helpers.UploadTo('returant/category')),
        ),
        migrations.AlterField(
            model_name='restaurantmenu',
            name='food_img',
            field=models.ImageField(null=True, upload_to=config.helpers.UploadTo('restaurant/food')),
        ),
        migrations.CreateModel(
            name='Seat_Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to=config.helpers.UploadTo('restaurant/seats'))),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.seat')),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.restaurant'),
        ),
        migrations.AddField(
            model_name='tablebook',
            name='seat',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seat', to='main.seat'),
        ),
    ]
