from django.urls import path
from .views import SearchRestaurant
urlpatterns = [
    path("restaurant/<str:query>/", SearchRestaurant.as_view())
]