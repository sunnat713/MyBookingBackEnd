from django.urls import path
from .views import UserView, user_login, user_logout, UserRetrieve
app_name = "client"

urlpatterns = [
    path("register/", UserView.as_view(), name="user-view"),
    path("me/<int:pk>/", UserRetrieve.as_view(), name="profile"),
    path('Login/', user_login, name="login"),
    path('Logout/', user_logout, name="logput")
]