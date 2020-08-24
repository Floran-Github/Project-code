from django.urls import path

from .views import StudentListView, StudentDeleteView, StudentDetailView, StudentUpdateView, StudentCreateView, StudentBulkUploadView,downloadcsv

urlpatterns = [
  path('list', StudentListView.as_view(), name='student-list'),
  path('<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
  path('create/', StudentCreateView.as_view(), name='student-create'),
  path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
  path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),

  path('upload/', StudentBulkUploadView.as_view(), name='student-upload'),
  path('downloadcsv/', downloadcsv, name='download-csv'),

]