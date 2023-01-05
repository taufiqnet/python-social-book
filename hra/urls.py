from django.urls import path, include
from django.views import generic
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    
    #Using Jquery for Department Insert, Update, Delete
    path('department/', views.department_data, name='department'),
    path('save/', views.save_data, name='save'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.edit_data, name='edit'),
    
    #For Rest Framework:
    path('api/', views.getRoutes),
    path('api/departments/', views.getDepartments),
    path('api/departments/create', views.createDepartment),
    path('api/departments/<str:pk>/update/', views.updateDepartment),
    path('api/departments/<str:pk>/delete/', views.deleteDepartment),
    path('api/departments/<str:pk>', views.getDepartment)
]
