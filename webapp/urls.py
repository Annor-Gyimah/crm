from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('my_login', views.my_login, name='my_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('user_logout',views.user_logout, name='user_logout'),

    # crud
    path('create_record/', views.create_employee, name='create_record'),
    path('update_record/<int:pk>', views.edit_employee, name='update_record'),
    path('view_record/<int:pk>', views.view_employee, name='view_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),

] 