from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_task, name='create_task'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]
