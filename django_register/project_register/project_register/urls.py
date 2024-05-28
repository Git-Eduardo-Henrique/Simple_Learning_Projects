from app_register import views

from django.urls import path

urlpatterns = [
    path("", views.home, name="home"), 
    path("users/", views.user, name="user_list")
]
