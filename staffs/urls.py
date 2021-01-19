from django.urls import path

from .views import *

urlpatterns = [
  path('list/', StaffListView.as_view(), name='staff-list'),
  path('<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
  path('create/', StaffCreateView.as_view(), name='staff-create'),
  path('<int:pk>/update/', StaffUpdateView.as_view(), name='staff-update'),
  path('<int:pk>/delete/', StaffDeleteView.as_view(), name='staff-delete'),
  path('downloadcsv', downloadcsv, name='staff-download-csv'),
  path('export', bulkUpload, name='staff-export'),
  path('import', csv_to_staff_database, name='staff-import'),

  path('head/list/', HeadListView.as_view(), name='head-list'),
  path('head/<int:pk>/', HeadDetailView.as_view(), name='head-detail'),
  path('head/create/', HeadCreateView.as_view(), name='head-create'),
  path('head/<int:pk>/update/', HeadUpdateView.as_view(), name='head-update'),
  path('head/<int:pk>/delete/', HeadDeleteView.as_view(), name='head-delete'),
]
