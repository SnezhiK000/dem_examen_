from django.contrib import admin
from django.urls import path
from appex import views

urlpatterns = [
    path('', views.login_view,name = 'login_view'),
    path('admin/', views.show_admin,name = 'show_admin'),
    path('manager/', views.show_manager,name = 'show_manager'),
    path('guest/', views.show_guest,name = 'show_guest'),
    path('manager/<int:id>/edit', views.edit_manager,name = 'edit_manager'),
]
