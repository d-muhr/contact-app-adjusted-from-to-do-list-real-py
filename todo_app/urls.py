# todo_list/todo_app/urls.py
from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("contact_list/<int:list_id>/", views.ContactListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("contact_list/add/", views.ListCreate.as_view(), name="list-add"),
    path(
        "contact_list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"
    ),
    # CRUD patterns for ToDoItems
    path(
        "contact_list/<int:list_id>/contact/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    path(
        "contact_list/<int:list_id>/contact/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update",
    ),
    path(
        "contact_list/<int:list_id>/contact/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    ),
]
