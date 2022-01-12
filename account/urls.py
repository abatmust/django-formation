from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("register", views.registerUser, name="register"),
    path("profiles", views.profiles, name="profiles-list"),
    path("profiles/<uuid:id>", views.show, name="show-profile"),
    path("edit-profile/<uuid:id>", views.edit, name="edit-profile"),
    path("update-profile/<uuid:id>", views.update, name="update-profile"),

]
