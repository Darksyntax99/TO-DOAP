from django.urls import path
from . import views
# Task app URLs
urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
