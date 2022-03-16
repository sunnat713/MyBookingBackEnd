from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    is_delivery = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.owner.username} {self.name}"

    class Meta:
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'


class MealCategory(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'meal_category'
        verbose_name_plural = 'meal_categories'


class Meal(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT)
    meal_category = models.ForeignKey(MealCategory, on_delete=models.RESTRICT)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'


FeatureChoice = (
    ('B', 'breakfast'),
    ('L', 'launch'),
    ('D', 'dinner'),
)
TimingChoice = (
    ('Sunday', 'sunday'),
    ('Monday', 'monday'),
    ('Tuesday', 'tuesday'),
    ('Wednesday', 'wednesday'),
    ('Thursday', 'thursday'),
    ('Friday', 'friday'),
    ('Saturday', 'saturday'),

)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT)
    meal_category = models.ForeignKey(MealCategory, on_delete=models.RESTRICT)
    meal = models.ForeignKey(Meal, on_delete=models.RESTRICT)
    features = models.CharField(choices=FeatureChoice, max_length=50)
    timing = models.CharField(choices=TimingChoice, max_length=50)
