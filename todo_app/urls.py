# todo_list/todo_app/urls.py
from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("contact/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("contact/add/", views.ListCreate.as_view(), name="list-add"),
    path(
        "contact/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"
    ),
    # CRUD patterns for ToDoItems
    path(
        "contact/<int:list_id>/info/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    path(
        "contact/<int:list_id>/info/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),
    path(
        "contact/<int:list_id>/info/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    ),
]
