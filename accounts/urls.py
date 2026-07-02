from django.urls import path

from accounts.views import register, user_login, user_logout
from .views import forgot_password, restore_password

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    path("forgot-password/", forgot_password, name="forgot_password"),
    path("restore-password/", restore_password, name="restore_password"),
]