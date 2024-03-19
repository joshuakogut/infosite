from django.contrib import admin
from django.urls import include, path, re_path

from . import views


urlpatterns = [
    # path("feed.tsv",                  views.feed, name="feed"),
    path("order/", include("order.urls")),
    path("product/", include("product.urls")),
    re_path(r"^.*/?$", views.index, name="index"),
    # path('admin/',                    admin.site.urls),
]
