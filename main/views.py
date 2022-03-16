from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsOwner

class SettingView(ListCreateAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (IsAuthenticated,)

class SettingRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = (IsAuthenticated,)


class RestaurantView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticated,)

class RestaurantRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsOwner, IsAuthenticated)

class RestaurantCategoryView(ListCreateAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer
    permission_classes = (IsAuthenticated,)

class RestaurantCategoryRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer
    permission_classes = (IsAuthenticated,)


class FoodCategoryView(ListCreateAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    permission_classes = (IsAuthenticated,)

class FoodCategoryRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    permission_classes = (IsAuthenticated,)


class RestaurantMenuView(ListCreateAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer
    permission_classes = (IsAuthenticated,)

class RestaurantMenuRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer
    permission_classes = (IsAuthenticated,)


class SeatView(ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAuthenticated,)

class SeatRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAuthenticated,)
    

#Bokking Events
class FoodBooking(ListCreateAPIView):
    queryset = FoodBook.objects.all()
    serializer_class = FoodBookSerializer
    permission_classes = (IsAuthenticated,)

class FoodBookRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = FoodBook.objects.all()
    serializer_class = FoodBookSerializer
    permission_classes = (IsAuthenticated,)

class SeatBooking(ListCreateAPIView):
    queryset = SeatBook.objects.all()
    serializer_class = SeatBookSerializer
    permission_classes = (IsAuthenticated,)

class SeatBookingRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = SeatBook.objects.all()
    serializer_class = SeatBookSerializer
    permission_classes = (IsAuthenticated,)

