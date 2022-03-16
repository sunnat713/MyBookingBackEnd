from .models import *
from rest_framework import serializers

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"

class RestaurantCategorySerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    class Meta:
        model = RestaurantCategory
        exclude = ("name_uz", "name_ru", "name_en")
        

class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = "__all__"

class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = "__all__"

class FoodBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodBook
        exclude = ("status",)
        read_only_fields = ("user",)
    
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

class SeatIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat_Img
        fields = "__all__"

class SeatBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatBook
        exclude = ("status",)
        read_only_fields = ("user",)

