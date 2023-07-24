
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.createTodo, name= 'create'),
    path('edit/<int:pk>/', views.editTodo, name= 'edit'),
    path('delete/<int:pk>/', views.deleteTodo, name= 'delete')
]
