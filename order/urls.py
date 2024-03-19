from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:order_number>", views.redirect, name="redirect"),
    path("<str:token>", views.status, name="status"),
]
