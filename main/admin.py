from django.contrib import admin
from .models import *


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'slug',
                    'owner',
                    'image',
                    'location',
                    'city',
                    'is_delivery', ]


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['meal_category', 'name', 'price', 'quantity', 'image', 'rating']


@admin.register(MealCategory)
class MealCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'restaurant', 'meal_category', 'meal']
