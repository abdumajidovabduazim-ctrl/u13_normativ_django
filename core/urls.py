from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
path('posts/', include('posts.urls')),
    path('api/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('api/', include('shop.urls')),
    path('', include('post.urls')),
    path('api/', include('post.urls')),

    path('i18n/', include('django.conf.urls.i18n')),
]