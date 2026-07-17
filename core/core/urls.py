from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import home


urlpatterns = [
    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path("shop/", include("shop.urls")),

    path("accounts/", include("accounts.urls")),

    path("posts/", include("posts.urls")),

    path("post-api/", include("post.urls")),

    path("api/", include("shop.urls")),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)