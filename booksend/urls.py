from django.urls import path
from . import views

urlpatterns = [
    path('', views.booksend_list, name='booksend_list'),
    path('add/', views.booksend_create, name='booksend_create'),
    path('<int:pk>/edit/', views.booksend_update, name='booksend_update'),
    path('<int:pk>/delete/', views.booksend_delete, name='booksend_delete'),
    path('export/csv/', views.booksend_export_csv, name='booksend_export_csv'),
]