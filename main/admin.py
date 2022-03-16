from django.contrib import admin
from .models import Setting, Restaurant, RestaurantCategory, RestaurantMenu, FoodCategory, FoodBook, SeatBook, Seat_Img, Seat
# Register your models here.

admin.site.register(Setting)
admin.site.register(Restaurant)
admin.site.register(RestaurantCategory)
admin.site.register(FoodCategory)
admin.site.register(RestaurantMenu)
admin.site.register(FoodBook)
admin.site.register(SeatBook)

class ImgInstatnceInine(admin.TabularInline):
    model = Seat_Img

class SeatAdmin(admin.ModelAdmin):
    inlines = [ImgInstatnceInine]

admin.site.register(Seat,SeatAdmin)