from django.urls import path
from .views import loginUser, logoutUser, registerUser, userDetail, userUpdate, userDelete

urlpatterns = [
    path("loginUser", loginUser, name="login"),
    path("logoutUser", logoutUser, name="logout"),
    path("register-user", registerUser, name="registerUser"),
    path("detail/<int:id>", userDetail, name="userDetail"),
    path("update/<int:id>", userUpdate, name="userUpdate"),
    path("delete/<int:id>", userDelete, name="userDelete"),

]