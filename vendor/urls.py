from django.urls import path 
from . import views
from accounts import views as AccountViews
urlpatterns = [
    path('',AccountViews.vendorDashboard, name='vendor'  ),
    path('profile/', views.vprofile, name='vprofile' ),
    path('menu-builder/', views.menu_builder, name='menu_builder'),
    path('menu-builder/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),

    # category crud
    path('menu-builder/category/add/', views.add_categor, name='add_categor'),
    path('menu-builder/category/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('menu-builder/category/delete/<int:pk>/', views.delete_category, name='delete_category'),
]
