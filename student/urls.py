from django.urls import path

from .views import *

urlpatterns = [
  path('list', StudentListView.as_view(), name='student-list'),
  path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
  path('create/', StudentCreateView.as_view(), name='student-create'),
  path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
  path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),

  path('upload/', StudentBulkUploadView.as_view(), name='student-upload'),
  path('downloadcsv/', downloadcsv, name='download-csv'),

  path('batch', BatchListView.as_view(), name='batch'),
  path('batch/create/', BatchCreate, name='batch-create'),
  path('batch/<int:pk>/', BatchStudentListView.as_view(), name='batch-student-list'),
  path('batch/delete/<int:pk>/', BatchDeleteView.as_view(), name='batch-delete'),


]