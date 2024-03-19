from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("feed.tsv", views.feed, name="feed"),
    path("img/<str:productid>", views.image, name="image"),
    path("<str:productid>", views.detail, name="detail"),
]
