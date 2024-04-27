from django.contrib import admin
from django.urls import path
from . import views

app_name = 'PORTFOLIO'

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login_view, name = "login"),
    path('user/', views.user_view, name = "user"),
    path('user/addproject/', views.add_project, name='addproject'),
    path('deleteproject/<int:id>/', views.delete_project, name='deleteproject'),
    path('updateproject/<int:id>/', views.update_project, name='updateproject'),
    path('logout/', views.custom_logout, name='logout'),
]