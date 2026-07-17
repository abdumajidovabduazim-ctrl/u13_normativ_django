from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import home


schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version="v1",
        description="JWT Authentication va Swagger",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),

    # Accounts
    path("accounts/", include("accounts.urls")),

    # Shop
    path("shop/", include("shop.urls")),

    # Eski posts app
    path("posts/", include("posts.urls")),

    # Normativ post API
    path("api/", include("post.urls")),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Swagger
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger",
    ),

    path("i18n/", include("django.conf.urls.i18n")),
]