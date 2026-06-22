from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
)

router = DefaultRouter()
router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]

urlpatterns += router.urls