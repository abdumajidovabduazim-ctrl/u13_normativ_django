from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    path('shop/', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('api/', include('shop.urls')),
    path('', include('post.urls')),

    # 🌐 Localization (til almashtirish)
    path('i18n/', include('django.conf.urls.i18n')),
]