from django.urls import include, path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Explicit URL: reverse('index') would resolve to the site root, since
    # portal/urls.py also names its root view 'index'.
    path("browse/", RedirectView.as_view(url="/product/", permanent=False)),
    path("img/<str:productid>", views.image, name="image"),
    path("<str:productid>", views.detail, name="detail"),
]
