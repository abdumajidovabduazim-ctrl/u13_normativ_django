from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('create/', views.create_post),

    path('<int:pk>/', views.post_detail, name='post_detail'),
]