from .models import *
from rest_framework import serializers
from client.serializers import UserSerializer

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"

class RestaurantCategorySerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    class Meta:
        model = RestaurantCategory
        exclude = ("name_uz", "name_ru", "name_en")

class RestaurantSerializer(serializers.ModelSerializer):
    # category = RestaurantCategorySerializer(many=True)
    
    class Meta:
        model = Restaurant
        fields = "__all__"

    def create(self, validated_data):
        validated_data['user'] = self._context['request'].user
        return super().create(validated_data)


class FoodCategorySerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()
    class Meta:
        model = FoodCategory
        exclude = ("name_uz", "name_ru", "name_en")

class RestaurantMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = "__all__"

    def create(self, validated_data):
        validated_data['restaurant'].user_id = self._context['request'].user.id
        return super().create(validated_data)

class FoodBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodBook
        exclude = ("status",)
        # read_only_fields = ('book_start', "book_end")

    def create(self, validated_data):
        validated_data['user'] = self._context['request'].user
        return super().create(validated_data)

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

class SeatIMGSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat_Img
        fields = "__all__"

class SeatBookSerializer(serializers.ModelSerializer):
    available_seats = serializers.ReadOnlyField()
    class Meta:
        model = SeatBook
        exclude = ("status",)
        # read_only_fields = ("user",)
    
    def create(self, validated_data):
        validated_data['user'] = self._context['request'].user
        return super().create(validated_data)

