from django.urls import path
from .views import LoginUser, LogoutUser, RegisterUser, GetAllUsers, GetUser

urlpatterns = [
    path("login/", LoginUser.as_view(), name="LoginUser"),
    path("logout/", LogoutUser.as_view(), name="LogoutUser"),
    path("register/", RegisterUser.as_view(), name="RegisterUser"),
    path("<int:id>/", GetUser.as_view(), name="GetUser"),
    path("", GetAllUsers.as_view(), name="GetAllUsers"),
]
