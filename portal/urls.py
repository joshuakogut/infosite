from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path

from . import views

urlpatterns = [
    # path("feed.tsv", views.feed, name="feed"),
    path("shelf/", include("shelf.urls")),
    path("order/", include("order.urls")),
    path("product/", include("product.urls")),
]

# Serve static files (style.css, logo, no-image.png). MUST be registered
# before the catch-all below: that re_path matches any non-empty path, so
# static requests appended after it would never be reached. Without this,
# /static/* fell through to views.index and returned "Hello world", leaving
# every page unstyled and images rendering at their intrinsic sizes.
# DEBUG-gated like Django's runserver static serving, so it never applies in
# production (collectstatic + web server should serve these instead).
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()

urlpatterns += [
    re_path(r"^.*/?$", views.index, name="index"),
    # path('admin/', admin.site.urls),
]
