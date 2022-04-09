from django.urls import path
from .views import  *

app_name = "main"

urlpatterns = [
    path("setting/", SettingView.as_view(), name="setting"),
    path("setting/<int:pk>/", SettingRetrieve.as_view(), name="setting-retrieve"),

    path("restaurant/", RestaurantView.as_view(), name="restaurant"),
    path("restaurant/<int:pk>/", RestaurantRetrieve.as_view(), name="restaurant-retrieve"),

    path('restaurant-by-category/<int:cat_id>/', RestaurantByCat.as_view(), name="restaurant-by-cat"),
    path("food-category-by-restaurant/<int:res_id>/", FoodCatBYRestaurant.as_view(), name="food-cat-by-res"),

    path("restaurant-category/", RestaurantCategoryView.as_view(), name="restaurant-category"),
    path("restaurant-category/<int:pk>/", RestaurantCategoryRetrieve.as_view(), name="restaurant-category-retrieve"),

    path("food-category/", FoodCategoryView.as_view(), name="food-category"),
    path("food-category/<int:pk>/", FoodCategoryRetrieve.as_view(), name="food-category-retrieve"),
    
    path("restaurant-menu/", RestaurantMenuView.as_view(), name="restaurant-menu"),
    path("restaurant-menu/<int:pk>/", RestaurantMenuRetrieve.as_view(), name="restaurant-menu-retrieve"),
    path("res-menu-by-restaurant/<int:res_id>/", ResMenuByRes.as_view(), name="res-menu-by-res"),

    path("seat/", SeatView.as_view(), name="seat"),
    path("seat/<int:pk>/", SeatRetrieve.as_view(), name="seat-retrieve"),
    path("seat-by-res/<int:res_id>/", SeatByRes.as_view(), name="seat-by-res"),

    path("food-booking/", FoodBooking.as_view(), name="food-book"),
    path("food-booking/<int:pk>/", FoodBookRetrieve.as_view(), name="food-book-retrieve"),
    path("food-book-by-res/<int:res_id>/", FoodBookByRes.as_view(), name="food-book-by-res"),

    path("seat-booking/", SeatBooking.as_view(), name="seat-book"),
    path("seat-booking/<int:pk>/", SeatBookingRetrieve.as_view(), name="seat-book-retrieve"),
    path("seat-book-by-res/<int:res_id>/", SeatBookByRes.as_view(), name="seat-book-by-res"),
    
    
]   
