from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import  Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsOwner, IsRestaurantOwner
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

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

class RestaurantByCat(APIView, PageNumberPagination):
    def get(self, request, cat_id):
        try:
            obj = Restaurant.objects.filter(category=cat_id)
        except:
            return Response("No data")
        result = self.paginate_queryset(obj,request,view=self)
        serialized = RestaurantSerializer(result, many=True, context={'request':request})
        return self.get_paginated_response({"data":serialized.data,"page_size":self.page_size})

class RestaurantCategoryView(ListCreateAPIView):
    queryset = RestaurantCategory.objects.all()
    serializer_class = RestaurantCategorySerializer
    # permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated, IsRestaurantOwner)

class FoodCatBYRestaurant(APIView, PageNumberPagination):
    def get(self, request, res_id):
        try:
            obj = FoodCategory.objects.filter(restaurant_id=res_id)
        except:
            return Response("No data")
        result = self.paginate_queryset(obj,request,view=self)
        serialized = FoodCategorySerializer(result, many=True, context={'request':request})
        return self.get_paginated_response({"data":serialized.data,"page_size":self.page_size})

class RestaurantMenuView(ListCreateAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer
    permission_classes = (IsAuthenticated,)

class RestaurantMenuRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = RestaurantMenu.objects.all()
    serializer_class = RestaurantMenuSerializer
    permission_classes = (IsAuthenticated, IsRestaurantOwner)

class ResMenuByRes(APIView, PageNumberPagination):
     def get(self, request, res_id):
        try:
            obj = RestaurantMenu.objects.filter(restaurant_id=res_id)
        except:
            return Response("No data")
        result = self.paginate_queryset(obj,request,view=self)
        serialized = RestaurantMenuSerializer(result, many=True, context={'request':request})
        return self.get_paginated_response({"data":serialized.data,"page_size":self.page_size})

class SeatView(ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAuthenticated,)

class SeatRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAuthenticated, IsRestaurantOwner)

class SeatByRes(APIView, PageNumberPagination):
    def get(self, request, res_id):
        try:
            obj = Seat.objects.filter(restaurant_id=res_id)
        except:
            return Response("No data")
        result = self.paginate_queryset(obj,request,view=self)
        serialized = SeatSerializer(result, many=True, context={'request':request})
        return self.get_paginated_response({"data":serialized.data,"page_size":self.page_size})


#Booking Events
class FoodBooking(ListCreateAPIView):
    queryset = FoodBook.objects.all()
    serializer_class = FoodBookSerializer
    permission_classes = (IsAuthenticated,)

class FoodBookRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = FoodBook.objects.all()
    serializer_class = FoodBookSerializer
    permission_classes = (IsAuthenticated, IsOwner)

class FoodBookByRes(APIView, PageNumberPagination):
    def get(self, request, res_id):
        try:
            obj = FoodBook.objects.filter(restaurant_id=res_id)
        except:
            return Response("No data")
        result = self.paginate_queryset(obj,request,view=self)
        serialized = FoodBookSerializer(result, many=True, context={'request':request})
        return self.get_paginated_response({"data":serialized.data,"page_size":self.page_size})

class SeatBooking(ListCreateAPIView):
    queryset = SeatBook.objects.all()
    serializer_class = SeatBookSerializer
    permission_classes = (IsAuthenticated,)

class SeatBookingRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = SeatBook.objects.all()
    serializer_class = SeatBookSerializer
    permission_classes = (IsAuthenticated, IsOwner)

class SeatBookByRes(APIView, PageNumberPagination):
    def get(self, request, res_id):
        try:
            obj = SeatBook.objects.filter(restaurant_id=res_id)
        except:
            return Response("No data")
        result = self.paginate_queryset(obj,request,view=self)
        serialized = SeatBookSerializer(result, many=True, context={'request':request})
        return self.get_paginated_response({"data":serialized.data,"page_size":self.page_size})
