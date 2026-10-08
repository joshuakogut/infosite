from django.urls import path
from . import views

urlpatterns = [
    path("", views.shelf_index, name="shelf_index"),
    path("wipe/", views.wipe, name="shelf_wipe"),
]
