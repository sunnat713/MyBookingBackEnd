# Generated by Django 4.0.3 on 2022-03-14 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_foodbook_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodbook',
            name='food',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='main.restaurantmenu'),
        ),
    ]
