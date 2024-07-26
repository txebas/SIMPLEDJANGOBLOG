from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('libros/', views.libro_list, name='libro_list'),
    path('libros/<int:pk>/', views.libro_detail, name='libro_detail'),

]