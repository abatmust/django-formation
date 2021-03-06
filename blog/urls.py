from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListArticleView.as_view(), name="list_of_article"),
    path("create/", views.CreateArticleView.as_view(), name="create_article"),
    path("edit/<int:id>/", views.EditArticleView.as_view(), name="edit_article"),
    path("delete/<int:id>/", views.delete, name="delete_article"),
    path("<slug:slug>/", views.ShowArticleView.as_view(), name="show_article"),
]
