from django.contrib import admin
from .models import Setting, Restaurant, RestaurantCategory, RestaurantMenu, FoodCategory, FoodBook, SeatBook, Seat_Img, Seat
# Register your models here.

admin.site.register(Setting)
admin.site.register(RestaurantCategory)
admin.site.register(FoodCategory)
admin.site.register(RestaurantMenu)
admin.site.register(FoodBook)
admin.site.register(SeatBook)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name',)
    filter_horizontal = ('category',)
admin.site.register(Restaurant, RestaurantAdmin)

class ImgInstatnceInine(admin.TabularInline):
    model = Seat_Img

class SeatAdmin(admin.ModelAdmin):
    inlines = [ImgInstatnceInine]

admin.site.register(Seat,SeatAdmin)