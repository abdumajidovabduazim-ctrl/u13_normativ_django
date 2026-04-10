from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_list, name='phone_list'),
    path('create/', views.phone_create, name='phone_create'),
    path('<int:pk>/update/', views.phone_update, name='phone_update'),
    path('<int:pk>/delete/', views.phone_delete, name='phone_delete'),
]