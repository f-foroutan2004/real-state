from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.property_create_view, name='property_create'),
    path('', views.property_list_view, name='property_list'),
    path('<int:pk>/', views.property_detail_view, name='property_detail'),
    path('<int:pk>/edit/', views.property_edit_view, name='property_edit'),
    path('<int:pk>/delete/', views.property_delete_view, name='property_delete'),
]