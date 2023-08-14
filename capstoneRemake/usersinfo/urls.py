from django.urls import path
from .views import loginUser, logoutUser, userRegister, userDetail, userUpdate, userDelete, userPing

urlpatterns = [
    path("loginUser", loginUser, name="login"),
    path("logoutUser", logoutUser, name="logout"),
    path("register", userRegister, name="userRegister"),
    path("detail/<int:id>", userDetail, name="userDetail"),
    path("update/<int:id>", userUpdate, name="userUpdate"),
    path("delete/<int:id>", userDelete, name="userDelete"),
    path("ping/<int:id>", userPing, name="userPing"),

]