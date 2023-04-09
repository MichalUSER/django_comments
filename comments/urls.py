from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_comment", views.add_comment, name="add_comment"),
    path("delete_comments", views.delete_comments, name="delete_comment")
]
