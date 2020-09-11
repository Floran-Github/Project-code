from django.urls import path

from .views import *

urlpatterns = [
  path('list/', ElementListView.as_view(), name='element-list'),
  path('<int:pk>/', ElementDetailView.as_view(), name='element-detail'),
  path('create/', ElementCreateView.as_view(), name='element-create'),
  path('<int:pk>/update/', ElementUpdateView.as_view(), name='element-update'),
  path('<int:pk>/delete/', ElementDeleteView.as_view(), name='element-delete'),

  path('submission/list/', SubmissionListView.as_view(), name='submission-list'),
  path('submission/<int:pk>/', SubmissionCreateView.as_view(), name='submission'),
  path('submission/<int:pk>/update/', SubmissionUpdateView.as_view(), name='submission-update'),
  path('submission/detail/<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),
  
  path('submitted/list/', SubimittedListView.as_view(), name='submit-list'),
  path('submitted/<int:pk>/', GradeView.as_view(), name='grade'),
  
]