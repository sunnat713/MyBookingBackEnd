from django.db import models
from config.helpers import UploadTo
from django.utils.translation import get_language

class Time(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Setting(models.Model):
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    info = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

class RestaurantCategory(Time):
    name_uz = models.CharField(max_length=120, null=True)
    name_ru = models.CharField(max_length=120, null=True)
    name_en = models.CharField(max_length=120, null=True)
    icon = models.ImageField(upload_to=UploadTo("returant/category"))

    @property
    def name(self):
        return getattr(self, f'name_{get_language()}')

class Restaurant(Time):
    owner = models.ForeignKey("client.User", on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField('RestaurantCategory')
    name = models.CharField(max_length=120, blank=True, null=True)
    logo = models.ImageField(upload_to=UploadTo("restaurant/logo"), null=True)
    location = models.URLField(blank=True, null=True)

#Food----------------------------
class FoodCategory(Time):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=120, null=True)
    name_ru = models.CharField(max_length=120, null=True)
    name_en = models.CharField(max_length=120, null=True)

    @property
    def name(self):
        return getattr(self, f'name_{get_language()}')

class RestaurantMenu(Time):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=True)
    food_category = models.ForeignKey('FoodCategory', on_delete=models.CASCADE)
    food_name = models.CharField(max_length=120, null=True)
    food_price = models.CharField(max_length=10, null=True)
    food_img = models.ImageField(upload_to=UploadTo("restaurant/food"), null=True)
    food_desc = models.TextField(null=True)
    food_desc_ru = models.TextField(null=True)


class FoodBook(Time):
    user = models.ForeignKey("client.User", on_delete=models.CASCADE, default=None)
    food = models.ForeignKey("RestaurantMenu", on_delete=models.CASCADE, default=None, related_name="food", null=True)
    amount = models.PositiveSmallIntegerField(default=0, null=True)
    status = models.CharField( max_length=4, choices=(("1","Done"), ("2", "Not yet"), ("3", "Doing")), default="2", null=True)
    book_start = models.DateTimeField(null=True)
    book_end = models.DateTimeField(null=True)


#CafeSEATS--------------------------------
# class SeatCategory(Time):
#     name_uz = models.CharField(max_length=120, null=True)
#     name_ru = models.CharField(max_length=120, null=True)
#     name_en = models.CharField(max_length=120, null=True)
#     icon = models.ImageField(UploadTo("returant/category"))

#     @property
#     def name(self):
#         return getattr(self, f'name_{get_language()}')

class Seat(Time):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=True)
    # seat_category = models.ForeignKey('SeatCategory', on_delete=models.CASCADE, null=True)
    name_uz = models.CharField(max_length=120, null=True)
    name_ru = models.CharField(max_length=120, null=True)
    name_en = models.CharField(max_length=120, null=True)
    desc = models.TextField(max_length=1000, null=True, blank=True)
    amount_seats = models.PositiveIntegerField(default=0, null=True, blank=True)

    @property
    def name(self):
        return getattr(self, f'name_{get_language()}')


class Seat_Img(models.Model):
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    img = models.ImageField(upload_to=UploadTo("restaurant/seats"), null=True, blank=True)


class SeatBook(Time):
    user = models.ForeignKey("client.User", on_delete=models.CASCADE, default=None)
    seat = models.ForeignKey("Seat", on_delete=models.CASCADE, default=None, related_name="seat", null=True)
    number_of_people = models.PositiveSmallIntegerField(default=0, blank=True)
    status = models.CharField( max_length=4, choices=(("1","Done"), ("2", "Not yet"), ("3", "Doing")), default="2", null=True)
    book_start = models.DateTimeField(null=True)
    book_end = models.DateTimeField(null=True)