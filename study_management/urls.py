

from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.study_add, name='study_add'),
    path('edit/<int:study_id>/', views.study_edit, name='study_edit'),
    path('view/<int:study_id>/', views.study_view, name='study_view'),
    path('delete/<int:study_id>/', views.study_delete, name='study_delete'),
    path('delete_multiple/', views.study_delete_multiple, name='study_delete_multiple'),  # Add this line
]
