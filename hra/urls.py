from django.urls import path, include
from django.views import generic
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save_data, name='save'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.edit_data, name='edit'),
]
